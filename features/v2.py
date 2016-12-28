import numpy as np
from message.message_pb2 import RequestV2, ResponseV2

def reqv2_proto_to_np(proto):
    stone_color_our = np.array(proto.stone_color_our._values, dtype='<i4').reshape((19, 19))
    stone_color_oppo = np.array(proto.stone_color_oppo._values, dtype='<i4').reshape((19, 19))
    stone_color_empty = np.array(proto.stone_color_empty._values, dtype='<i4').reshape((19, 19))
    turns_since_1 = np.array(proto.turns_since_one._values, dtype='<i4').reshape((19, 19))
    turns_since_2 = np.array(proto.turns_since_two._values, dtype='<i4').reshape((19, 19))
    turns_since_3 = np.array(proto.turns_since_three._values, dtype='<i4').reshape((19, 19))
    turns_since_4 = np.array(proto.turns_since_four._values, dtype='<i4').reshape((19, 19))
    turns_since_5 = np.array(proto.turns_since_five._values, dtype='<i4').reshape((19, 19))
    turns_since_6 = np.array(proto.turns_since_six._values, dtype='<i4').reshape((19, 19))
    turns_since_7 = np.array(proto.turns_since_seven._values, dtype='<i4').reshape((19, 19))
    turns_since_more = np.array(proto.turns_since_more._values, dtype='<i4').reshape((19, 19))
    liberties_our_1 = np.array(proto.liberties_our_one._values, dtype='<i4').reshape((19, 19))
    liberties_our_2 = np.array(proto.liberties_our_two._values, dtype='<i4').reshape((19, 19))
    liberties_our_3 = np.array(proto.liberties_our_three._values, dtype='<i4').reshape((19, 19))
    liberties_our_more = np.array(proto.liberties_our_more._values, dtype='<i4').reshape((19, 19))

    liberties_oppo_1 = np.array(proto.liberties_oppo_one._values, dtype='<i4').reshape((19, 19))
    liberties_oppo_2 = np.array(proto.liberties_oppo_two._values, dtype='<i4').reshape((19, 19))
    liberties_oppo_3 = np.array(proto.liberties_oppo_three._values, dtype='<i4').reshape((19, 19))
    liberties_oppo_more = np.array(proto.liberties_oppo_more._values, dtype='<i4').reshape((19, 19))

    capture_size_1 = np.array(proto.capture_size_one._values, dtype='<i4').reshape((19, 19))
    capture_size_2 = np.array(proto.capture_size_two._values, dtype='<i4').reshape((19, 19))
    capture_size_3 = np.array(proto.capture_size_three._values, dtype='<i4').reshape((19, 19))
    capture_size_4 = np.array(proto.capture_size_four._values, dtype='<i4').reshape((19, 19))
    capture_size_5 = np.array(proto.capture_size_five._values, dtype='<i4').reshape((19, 19))
    capture_size_6 = np.array(proto.capture_size_six._values, dtype='<i4').reshape((19, 19))
    capture_size_7 = np.array(proto.capture_size_seven._values, dtype='<i4').reshape((19, 19))
    capture_size_more = np.array(proto.capture_size_more._values, dtype='<i4').reshape((19, 19))

    self_atari_1 = np.array(proto.self_atari_one._values, dtype='<i4').reshape((19, 19))
    self_atari_2 = np.array(proto.self_atari_two._values, dtype='<i4').reshape((19, 19))
    self_atari_3 = np.array(proto.self_atari_three._values, dtype='<i4').reshape((19, 19))
    self_atari_4 = np.array(proto.self_atari_four._values, dtype='<i4').reshape((19, 19))
    self_atari_5 = np.array(proto.self_atari_five._values, dtype='<i4').reshape((19, 19))
    self_atari_6 = np.array(proto.self_atari_six._values, dtype='<i4').reshape((19, 19))
    self_atari_7 = np.array(proto.self_atari_seven._values, dtype='<i4').reshape((19, 19))
    self_atari_more = np.array(proto.self_atari_more._values, dtype='<i4').reshape((19, 19))

    sensibleness = np.array(proto.sensibleness._values, dtype='<i4').reshape((19, 19))
    ko = np.array(proto.ko._values, dtype='<i4').reshape((19, 19))

    border = np.array(proto.border._values, dtype='<i4').reshape((19, 19))

    position = np.array(proto.position._values, dtype='<f4').reshape((19, 19))

    return np.array([stone_color_our, stone_color_oppo, stone_color_empty,
                     turns_since_1, turns_since_2, turns_since_3, turns_since_4,
                     turns_since_5, turns_since_6, turns_since_7, turns_since_more,
                     liberties_our_1, liberties_our_2, liberties_our_3, liberties_our_more,
                     liberties_oppo_1, liberties_oppo_2, liberties_oppo_3, liberties_oppo_more,
                     capture_size_1, capture_size_2, capture_size_3, capture_size_4,
                     capture_size_5, capture_size_6, capture_size_7, capture_size_more,
                     self_atari_1, self_atari_2, self_atari_3, self_atari_4,
                     self_atari_5, self_atari_6, self_atari_7, self_atari_more,
                     sensibleness, ko, border, position])


def respv2_np_to_proto(arr):
    respV2 = ResponseV2()
    respV2.board_size = 361
    respV2.possibility.extend(arr.flatten().tolist())
    return respV2