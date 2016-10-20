# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    mid = np.transpose(np.vstack((x,y)))
    np.random.shuffle(mid)
    x_ = mid[:,0]
    y_ = mid[:,1]
    x_train, x_test = x_[:int(len(x)*ratio)], x_[int(len(x)*ratio):]
    y_train, y_test = y_[:int(len(y)*ratio)], y_[int(len(y)*ratio):]
    return x_train, y_train, x_test, y_test
