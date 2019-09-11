# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:59:04 2018

@author: libingrui
"""

import warnings
warnings.filterwarnings('ignore')
from mlp import BaseMLP
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler as SS
from sklearn.cross_validation import cross_val_score
from keras.utils import np_utils, generic_utils

def test_deep():
    model=BaseMLP(n_hidden=40,n_deep=3, l1_norm=0, drop=0.1, verbose=1)
    model.load(r'D:\work\DL_Predicting_Pharmacological\data\result_file\gctx\train_testout.txt')
    model.predict(test_data)
    