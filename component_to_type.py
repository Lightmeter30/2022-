# -*- coding: utf-8 -*-
# @Time    : 2022/9/17 11:06
# @Author  : LuMing
# @File    : component_to_type.py
# @Software: PyCharm 
# @Comment :


import numpy as np
import pandas as pd

from bpnn import Bpnn


def train():
    df = pd.read_excel("unit.xlsx", "Sheet1")
    matrix = np.array(df)
    label = []
    data = []
    for line in matrix:
        data.append(line[15:] / 100)
        label.append(line[4:6])
    my_bpnn = Bpnn(14, 20, 2)
    my_bpnn.train(data, label, 20000)
    my_bpnn.test(data, label)
    my_bpnn.saveMatrix("weight_xh_ct", "weight_hy_ct")


def predict(data):
    my_bpnn = Bpnn(14, 20, 2)
    my_bpnn.getWeightFromXlsx("weight_xh_ct.xls", "weight_hy_ct.xls")
    result = my_bpnn.predict(data)
    if result[0] > result[1]:
        print("高钾")
    else:
        print("铅钡")


def main():
    predict([36.28,	0,	1.05,	2.34,	1.18,	5.73,	1.86,	0.26,	47.43,	0,	3.57,	0.19,	0,	0])


if __name__ == '__main__':
    main()
