import numpy as np
import scipy.io

import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import invgamma
import scipy.stats as stats

# Particle Gibbs for BSP Forest Regression


from .bsp_utility import *
from .bsp_p_class import *


def BSP_Forest_fun():
    IterationTime = 40

    mTree = 50
    budget_val = 0.5
    testt = 0
    wi = 0

    dataNum = 500  # dataNum: 2000, 200

    dimNum = 5 # requie dimNum >5
    [xdata, ydata] = Friedman_function_gen(dimNum, dataNum)

    BSPF_Main(IterationTime, mTree, budget_val, xdata, ydata)

def BSPF_Main(IterationTime, mTree, budget_val, xdata, ydata):

    dimNum = xdata.shape[1]
    particleNUm = 20
    train_test_ratio = 0.5

    xdata_train, ydata_train, xdata_test, ydata_test, ydata_train_mean, dd, hyper_sigma_1, hyper_sigma_2, variance_hat = pre_process_data(xdata, ydata, train_test_ratio)

    mus = 0
    maxStage = 10
    add_dts_v = add_dts(mTree, mus, variance_hat, maxStage, budget_val, xdata_train, ydata_train, dimNum)

    startIte = int(IterationTime/2)
    for itei in range(IterationTime):

        predicted_y_train = np.zeros((add_dts_v.mTree, len(ydata_train)))
        predicted_y_test = np.zeros((add_dts_v.mTree, len(ydata_test)))

        add_dts_v.updates(particleNUm, maxStage, xdata_train, ydata_train, dimNum, hyper_sigma_1, hyper_sigma_2)
        print('Iteration '+str(itei)+' finished. ')

        for mi in range(add_dts_v.mTree):
            predicted_y_train[mi] = add_dts_v.add_dts[mi].assign_to_data(len(add_dts_v.add_dts[mi].z_label) - 1)
            predicted_y_test[mi] = add_dts_v.add_dts[mi].predict_data(xdata_test)


        y_train_itei = np.sum(predicted_y_train, axis=0)
        y_test_itei = np.sum(predicted_y_test, axis=0)

        if (itei>=startIte):

            if itei == startIte:
                stand_train = copy.copy(y_train_itei)
                stand_test = copy.copy(y_test_itei)

            else:
                stand_train = (stand_train*(itei-startIte)+y_train_itei)/(itei-startIte+1)
                stand_test = (stand_test*(itei-startIte)+y_test_itei)/(itei-startIte+1)

