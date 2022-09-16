# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 9:05
# @Author  :
# @File    : 关系检验.py
# @Software: PyCharm 
# @Comment : 2022CUMCM c题卡方分析


import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# 命名参照下面四行的注释
d = {'A': 0, 'B': 1, 'C': 2}  # decorate 纹饰
t = {'高钾': 0, '铅钡': 1}  # type 类型
c = {'蓝绿': 0, '浅蓝': 1, '紫': 2, '深绿': 3, '深蓝': 4, '浅绿': 5, '黑': 6, '绿': 7}  # color 颜色
w = {'无风化': 0, '风化': 1}  # weathering 风化


def statistics():
    df = pd.read_excel("data.xlsx", "表单1")
    df = df.fillna(0)
    matrix = np.array(df)
    # print(matrix)
    # 统计纹饰与风化的关系 w ==》 weathering
    w_decorate = np.zeros((2, 3), int)
    w_type = np.zeros((2, 2), int)
    w_color = np.zeros((2, 8), int)
    for line in matrix:
        w_decorate[w[line[4]]][d[line[1]]] += 1
        w_type[w[line[4]]][t[line[2]]] += 1
        if line[3] != 0:
            w_color[w[line[4]]][c[line[3]]] += 1
    return w_decorate, w_type, w_color


def kappa():
    w_decorate, w_type, w_color = statistics()
    print("wd=\n", w_decorate)
    print("wt=\n", w_type)
    print("wc=\n", w_color)
    wd_kt = chi2_contingency(w_decorate)
    wt_kt = chi2_contingency(w_type)
    wc_kt = chi2_contingency(w_color)
    return wd_kt, wt_kt, wc_kt


def main():
    wd_kt, wt_kt, wc_kt = kappa()
    print()
    print('wd卡方值=%.4f, p值=%.4f, 自由度=%i \nexpected_frep=\n%s\n' % wd_kt)
    print('wt卡方值=%.4f, p值=%.4f, 自由度=%i \nexpected_frep=\n%s\n' % wt_kt)
    print('wc卡方值=%.4f, p值=%.4f, 自由度=%i \nexpected_frep=\n%s\n' % wc_kt)


if __name__ == '__main__':
    main()
