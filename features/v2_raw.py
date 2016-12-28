import numpy as np
import sys
import os

def raw_v2_req_to_arr(raw):
    try:
        assert(len(raw) == 38 * 19 * 19 + 4 * 19 * 19)
        part1 = np.frombuffer(raw[:38*19*19], dtype='bool_').astype('float32').reshape((38, 19, 19))
        part2 = np.frombuffer(raw[38 * 19 * 19:], dtype='<f4').reshape((1, 19, 19))
        return np.concatenate((part1, part2))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        raise RuntimeError('Conversion error: {}'.format(e))