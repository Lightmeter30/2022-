# -*- coding: utf-8 -*-
# @Time    : 2022/9/17 11:05
# @Author  : LuMing
# @File    : type_to_component.py
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
        label.append(line[15:] / 100)
        data.append(line[1:15])
    my_bpnn = Bpnn(14, 20, 14)
    my_bpnn.train(data, label, 20000)
    my_bpnn.test(data, label)
    my_bpnn.saveMatrix("weight_xh_tc", "weight_hy_tc")
    my_bpnn.predict(data[0])


def predict(data):
    my_bpnn = Bpnn(14, 20, 14)
    my_bpnn.getWeightFromXlsx("weight_xh_tc.xls", "weight_hy_tc.xls")
    return my_bpnn.predict(data)


def main():
    print(predict(data=[1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]))


if __name__ == '__main__':
    main()
