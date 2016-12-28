import numpy as np
from message.message_pb2 import RequestV1, ResponseV1

def reqv1_proto_to_np(proto):
    our_lib1 = np.array(proto.our_group_lib1._values, dtype='<i4').reshape((19, 19))
    our_lib2 = np.array(proto.our_group_lib2._values, dtype='<i4').reshape((19, 19))
    our_lib3_plus = np.array(proto.our_group_lib3_plus._values, dtype='<i4').reshape((19, 19))
    oppo_lib1 = np.array(proto.oppo_group_lib1._values, dtype='<i4').reshape((19, 19))
    oppo_lib2 = np.array(proto.oppo_group_lib2._values, dtype='<i4').reshape((19, 19))
    oppo_lib3_plus = np.array(proto.oppo_group_lib3_plus._values, dtype='<i4').reshape((19, 19))
    is_simple_ko = np.array(proto.is_simple_ko._values, dtype='<i4').reshape((19, 19))
    return np.array([our_lib1, our_lib2, our_lib3_plus, oppo_lib1, oppo_lib2, oppo_lib3_plus, is_simple_ko])

def respv1_np_to_proto(arr):
    respV1 = ResponseV1()
    respV1.board_size = 361
    respV1.possibility.extend(arr.flatten().tolist())
    return respV1