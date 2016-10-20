# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lamb):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    a,b = tx.shape
    tr = np.transpose(tx)
    return np.dot(np.dot(np.linalg.inv(np.dot(tr,tx)+lamb*np.identity(b)),tr),y)
