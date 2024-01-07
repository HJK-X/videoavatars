
import cv2
import h5py
import argparse
import numpy as np
import chumpy as ch
import pickle as pkl
import os


a = ch.Ch(np.array([0]))


E = {
    'mask': a - a.r,
    'test': a - 5
}

x0 = [a]

print(a, a.r)

def test(b):
    print(a, a.r, b)

ch.minimize(
    E,
    x0,
    method='dogleg',
    options={
        'e_3': .01,
    },
    callback=test
)
print(x0)
print(a)