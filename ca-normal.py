# Simple CA simulator in Python

#

# *** Game of Life Rule ***

#

# Copyright 2008-2012 Hiroki Sayama

# sayama@binghamton.edu# Simple CA simulator in Python
#
# *** Game of Life Rule ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 100
height = 100
initProb = 0.2
kStart = 3.3
x0 = 0.01
kDelta = 0.005
r = 1

def f(k, x):
    return k * x * (1 - x)

def init():
    global time, config, nextConfig
    global k
    global avg

    avg = 0
    time = 0
    k = kStart
    
    config = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
            config[y, x] = RD.random()

    nextConfig = SP.zeros([height, width])

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time) + ' average = ' + str(avg))

def step():
    global time, config, nextConfig, avg

    time += 1
    avg = 0
    for x in xrange(width):
        for y in xrange(height):
            currentState = config[y, x]
            newState = f(k, currentState)
            nextConfig[y, x] = newState
            avg += newState
    avg /= width * height
    config, nextConfig = nextConfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
