# -*- coding: utf-8 -*-
def derivs(x, y):
    return list(i for i in y)

def rk4(y, x, dydx, h, derivs, n):
    hh = h*0.5
    h6 = h/6.0
    xh = x + hh
    yt = list(y[i] + hh*dydx[i] for i in range(n))
    dyt = derivs(xh, yt)
    yt = list(y[i] + hh*dyt[i] for i in range(n))
    dym = derivs(xh, yt)
    for i in range(n):
        yt[i] = y[i] + h*dym[i]
        dym[i] += dyt[i]
    dyt = derivs(x+h, yt)
    return list(y[i] + h6*(dydx[i] + dyt[i] + 2.0*dym[i]) for i in range(n))
