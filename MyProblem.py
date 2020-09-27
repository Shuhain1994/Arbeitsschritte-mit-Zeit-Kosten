# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea


"""
       
"""


class MyProblem ( ea.Problem ):
    def __init__(self):
        name = 'MyProblem'
        M = 2
        maxormins = [0,0]
        Dim = 8
        varTypes = [1] * Dim
        lb = [0] * Dim
        ub = [2] * Dim
        lbin = [1] * Dim
        ubin = [1] * Dim

        ea.Problem.__init__ ( self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin )
        # Add a new attribute to store machine coordinates
        self.a =np.random.randint(0,3,size=[3,8])

        self.z= np.copy ( self.a )
        self.z[self.a == 0]=2
        self.z[self.a == 1]=3
        self.z[self.a == 2]=4

        self.k= np.copy ( self.a )
        self.k[self.a == 0] = 3
        self.k[self.a == 1] = 2
        self.k[self.a == 2] = 4

    def aimFunc(self, pop):
        x = pop.Phen.astype ( int )
        f1 = np.sum ( self.k[x, [0, 1, 2, 3, 4, 5, 6, 7]], 1 )
        f2 = np.sum ( self.z[x, [0, 1, 2, 3, 4, 5, 6, 7]], 1 )

        pop.CV = np.array ( [np.sum ( self.k[x, [0, 1, 2, 3, 4, 5, 6, 7]], 1 )] ).T - 24
        pop.ObjV = np.vstack ( [f1, f2] ).T