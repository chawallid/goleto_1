import numpy as np


def smooth_x(wave, x, s, g,):
    xx = x.shape[0]
    xy = x.shape[1]
    smooth = np.zeros([xx, xy])
    for i in range(s+1, xy-s):
        sa = np.mean(x[:, int(i - s):int(i + s)], axis=1)
        smooth[:, i] = sa
    return smooth
