#!/usr/bin/python3
from __future__ import print_function
from message.message_pb2 import RequestV1, RequestV2, ResponseV1, ResponseV2
import tensorflow as tf
import numpy as np
import yaml
from keras.models import model_from_yaml
import os
import socket
from struct import pack
from features.v1 import reqv1_proto_to_np, respv1_np_to_proto
from features.v2 import reqv2_proto_to_np, respv2_np_to_proto
from features.v2_raw import raw_v2_req_to_arr

def load_model_and_weights(model_name = 'model.yml', weights_name = 'weights.hd5'):
    with open(os.path.join('model', model_name), 'r') as f:
        yml = yaml.load(f)
        model = model_from_yaml(yaml.dump(yml))
        model.load_weights(os.path.join('model', weights_name))
        model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])
        return model

def handle_sock(sock, addr, model):
    size_bytes = sock.recv(8)
    size = int.from_bytes(size_bytes, byteorder='little')
    print('message size is ', size)

    np.set_printoptions(linewidth=120)
    chunks = []
    bytes_recd = 0
    while bytes_recd < size:
        chunk = sock.recv(min(size - bytes_recd, 2048))
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    message_bytes = b''.join(chunks)

    np_arr_req = None
    try:
        np_arr_req = raw_v2_req_to_arr(message_bytes)
        #print(np.log(np_arr_req[-1]))
        if np_arr_req.shape[0] != 19:
            np_arr_req = np.swapaxes(np_arr_req, 0, 2)
            np_arr_req = np.swapaxes(np_arr_req, 0, 1)
    except Exception as e:
        print('Invalid format: ', e)
        sock.close()
        return


    pred = model.predict(np.array([np_arr_req]))[0]
    #print(pred.reshape((19, 19)))
    #print('generate resp')
    respV2 = respv2_np_to_proto(pred)

    str = respV2.SerializeToString()
    #print('Sending back...')
    size_bytes = pack('<q', len(str))

    #print('sending ', len(str))
    sock.sendall(size_bytes)
    sock.sendall(str)
    #print('OK')
    sock.close()

def run_server(model, port):
    print('Listening on port ', port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(64)

    while True:
        sock, addr = s.accept()
        print('Accepting new connection at ', addr)
        try:
            handle_sock(sock, addr, model)
        except Exception as e:
            print('Exception thrown')
            print(e)

if __name__ == '__main__':
    model = load_model_and_weights('k_bot.yml', '40_feature_v3.hd5')
    run_server(model, 7591)
