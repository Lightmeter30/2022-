# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 17:49
# @Author  : LuMing
# @File    : 线性规划.py
# @Software: PyCharm 
# @Comment :

from scipy import optimize
import pulp
import numpy as np


def main():
    # scipy库
    c = np.array([4, -1])
    A = np.array([[-1, 1], [-1, -1]])
    b = np.array([5, 0])
    x = (None, 3)
    y = (None, None)
    res = optimize.linprog(c, A, b, bounds=(x, y))
    print(res)

    # pulp库
    myProblem = pulp.LpProblem(sense=pulp.LpMaximize)

    x1 = pulp.LpVariable('x1', lowBound=0, upBound=None, cat='Continuous')
    x2 = pulp.LpVariable('x2', lowBound=0, upBound=None, cat='Continuous')
    x3 = pulp.LpVariable('x3', lowBound=0, upBound=None, cat='Continuous')

    myProblem += 2 * x1 + 3 * x2 - 5 * x3
    myProblem += (x1 + x2 + x3 == 7)
    myProblem += (2 * x1 - 5 * x2 + x3 >= 10)
    myProblem += (x1 + 3 * x2 + x3 <= 12)

    myProblem.solve()
    for i in myProblem.variables():
        print(i.name, '=', i.varValue)
    print('F(x)=', pulp.value(myProblem.objective))


if __name__ == '__main__':
    main()
