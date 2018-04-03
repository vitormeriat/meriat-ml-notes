#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Funções para regressão linear
def computeCost(X, y, w):
    m = y.size
    J = 0
    for i in range(m):
        J += np.square(X[i, :].dot(w) - y[i])
    J /= (2 * m)
    return (J)


def gradientDescent(X, y, w, alpha, num_iters):
    m = y.size
    J_history = np.zeros(num_iters)
    temp = np.zeros(w.size)
    numParameters = w.size

    for iter in range(num_iters):
        for j in range(numParameters):
            delta_j = 0
            for i in range(m):
                delta_j += (X[i, :].dot(w) - y[i]) * X[i, j]
            temp[j] = w[j] - alpha * (delta_j / m)
        w = temp
        J_history[iter] = computeCost(X, y, w)

    return (w, J_history)


# Funções para regressão logística
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def computeCost2(X, y, w):
    m = y.size
    J = 0
    for i in range(m):
        J += np.square(sigmoid(X[i, :].dot(w)) - y[i])
    J /= (2 * m)
    return (J)

def gradientDescent2(X, y, w, alpha, num_iters):
    m = y.size
    J_history = np.zeros(num_iters)
    temp = np.zeros(w.size)
    numParameters = w.size

    for iter in range(num_iters):
        for j in range(numParameters):
            delta_j = 0
            for i in range(m):
                delta_j += (sigmoid(X[i, :].dot(w)) - y[i]) * X[i, j]
            temp[j] = w[j] - alpha * (delta_j / m)
        w = temp
        J_history[iter] = computeCost2(X, y, w)

    return (w, J_history)


def geraDados2DfronteiraNonLinear(N=100):
    # draw N random points in the [0,1]x[0,1] square

    x1 = np.random.rand(N)
    x2 = np.random.rand(N)
    X = np.vstack(zip(np.ones(N),x1, x2))
    print("Shape do X: ", X.shape)

    # use cosine to define positive and negative classes
    y = np.array([1 if np.cos(2*np.pi*X[i,1]) / 2 + 0.5 > X[i,2] \
                  else 0 for i in range(N)])
    print("Shape do y: ", y.shape)

    p = plt.figure(figsize=(12,5))
    p1 = p.add_subplot(121)
    p1.plot(x1,x2,'o')

    # create a cosine curve and add to the plot
    x = np.arange(0, 1.0, 0.01)
    fx = np.cos(2*np.pi*x) / 2 + 0.5
    p1.plot(x, fx, lw=2)

    # discriminate those above and below the curve
    p2 = p.add_subplot(122)
    for i in range(N):
        if y[i]==1:
            p2.plot(x1[i],x2[i],'bo')  # o (bolinhas) azuis (blue)
        else:
            p2.plot(x1[i],x2[i],'ro')  # o (bolinhas) vermelhas (red)
                
    p2.plot(x, fx, lw=2)
    plt.show()
    
    return X, y, x, fx
