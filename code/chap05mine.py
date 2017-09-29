from __future__ import print_function, division


import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt

import thinkplot

from Cell1D import Cell1D, Cell1DViewer


# 3
rule = 110
n = 200
ca = Cell1D(rule, n, m=700)
ca.start_string('00010011011111'*50)
ca.loop(n-1)
np.savetxt('chap05-07.csv', ca.array, fmt='%d', delimiter=',')
viewer = Cell1DViewer(ca)
viewer.draw()
plt.savefig('chap05-8.jpg')
plt.savefig('chap05-8.pdf')
