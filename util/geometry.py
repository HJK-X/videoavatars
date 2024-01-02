import cv2
import numpy as np
import scipy.sparse as sp
from chumpy.utils import row, col
from chumpy import *
import chumpy as ch
from chumpy.ch import MatVecMult

class Rodrigues(Ch):
    dterms = 'rt'
    
    def compute_r(self):
        return cv2.Rodrigues(self.rt.r)[0]
    
    def compute_dr_wrt(self, wrt):
        if wrt is self.rt:
            return cv2.Rodrigues(self.rt.r)[1].T