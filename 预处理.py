# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 19:40
# @Author  : LuMing
# @File    : 预处理.py
# @Software: PyCharm 
# @Comment :

import pandas as pd
import numpy as np
import xlwt

w = {'未风化': 0, '无风化': 0, '风化': 1}
d = {'A': 0, 'B': 1, 'C': 2}  # decorate 纹饰
t = {'高钾': 0, '铅钡': 1}  # type 类型
c = {'蓝绿': 0, '浅蓝': 1, '紫': 2, '深绿': 3, '深蓝': 4, '浅绿': 5, '黑': 6, '绿': 7}  # color 颜色

unit_label = ['编号',	'A',	'B',	'C',	'高钾',	'铅钡',	'蓝绿',	'浅蓝',	'紫',	'深绿',	'深蓝',	'浅绿',	'黑',	'绿',	'表面风化',	'二氧化硅(SiO2)',	'氧化钠(Na2O)',	'氧化钾(K2O)',	'氧化钙(CaO)',	'氧化镁(MgO)',	'氧化铝(Al2O3)',	'氧化铁(Fe2O3)',	'氧化铜(CuO)',	'氧化铅(PbO)',	'氧化钡(BaO)',	'五氧化二磷(P2O5)',	'氧化锶(SrO)',	'氧化锡(SnO2)',	'二氧化硫(SO2)']

def read():
    df1 = pd.read_excel("data.xlsx", "表单1")
    df2 = pd.read_excel("data.xlsx", "表单2")
    df1 = df1.fillna(0)
    df2 = df2.fillna(0)
    matrix1 = np.array(df1)
    matrix2 = np.array(df2)
    return matrix1, matrix2


def isWeathering(line1, line2):
    if str(line2).__contains__("未风化"):
        return 0
    elif str(line2).__contains__("风化"):
        return 1
    else:
        return w[line1[14]]


def append(new_line, elems):
    for item in elems:
        new_line.append(item)


def unit():
    matrix1, matrix2 = read()
    u_matrix = []
    for line2 in matrix2:
        new_line = []
        no = int(str(line2[0])[0:2])
        line1 = matrix1[no - 1]
        line1 = to_bin(line1)
        # new_line.append(line1[0:4])
        append(new_line, line1[0:14])
        new_line.append(isWeathering(line1, line2))
        # new_line.append(line2[1:15])
        append(new_line, line2[1:15])
        u_matrix.append(new_line)
    return u_matrix


def save(rows, name, label):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet")
    for i in range(len(label)):
        sheet.write(0, i, label[i])

    for i in range(1, len(rows) + 1):
        for j in range(len(rows[i - 1])):
            sheet.write(i, j, rows[i - 1][j])

    workbook.save(name + ".xls")


def to_bin(line):
    new_line = []
    new_line.append(line[0])
    for i in range(3):
        if d[line[1]] == i:
            new_line.append(1)
        else:
            new_line.append(0)
    for i in range(2):
        if t[line[2]] == i:
            new_line.append(1)
        else:
            new_line.append(0)
    for i in range(8):
        if line[3] == 0:
            new_line.append(0)
        elif c[line[3]] == i:
            new_line.append(1)
        else:
            new_line.append(0)
    new_line.append(line[4])
    return new_line


def sort(sortLineNum, u_matrix):
    # 按照列号分类
    matrix1 = []
    matrix2 = []
    for line in u_matrix:
        if line[sortLineNum] == 1:
            matrix1.append(line)
        else:
            matrix2.append(line)
    return matrix1, matrix2


def main():
    df = pd.read_excel("铅钡.xls", "Sheet")
    matrix1, matrix2 = sort(14, np.array(df))
    save(matrix1, "铅钡风化", label=unit_label)
    save(matrix2, "铅钡未风化", label=unit_label)


if __name__ == '__main__':
    main()
