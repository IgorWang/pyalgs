#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author igor
# Created by iFantastic on 16-5-25
'''
递归样例：介乘公式

$$ f(x)=\left\{
\begin{aligned}
1  \\
n*(n-1) ! \\
\end{aligned}
\right.
$$

'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



