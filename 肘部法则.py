# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 23:04
# @Author  : LuMing
# @File    : 肘部法则.py
# @Software: PyCharm 
# @Comment :
import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def main():
    df_matrix = np.array(pd.read_excel("铅钡.xls", "Sheet"))
    data = df_matrix[15:]
    data_scaled = preprocessing.scale(data)
    distortions = []
    for i in range(1, 15):
        km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
        km.fit(data_scaled)
        distortions.append(km.inertia_)
    plt.figure(dpi=150)
    plt.plot(range(14), distortions, marker='o')
    plt.xlabel("Number of clusters")
    plt.ylabel("Distortion")
    plt.show()


if __name__ == '__main__':
    main()
