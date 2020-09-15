# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea

"""
     Angenommen, es gibt fünf Anlagen (A,B,C,D,E) in der Fabrik. 
     Finden Sie jetzt den kürzesten Weg durch diese fünf Anlagen, 
     ausgehend von A und schließlich zurück zu A.
      X  Y
    [[0, 0],
     [5, 12],
     [7, 9],
     [11, 29],
     [15, 13]    
"""


class MyProblem ( ea.Problem ):
    def __init__(self):
        name = 'MyProblem'
        M = 1
        maxormins = [1]
        Dim = 4
        varTypes = [1] * Dim
        lb = [1] * Dim
        ub = [4] * Dim
        lbin = [1] * Dim
        ubin = [1] * Dim

        ea.Problem.__init__ ( self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin )
        # Add a new attribute to store machine coordinates
        self.places = np.array ( [[0, 0],
                                  [5, 12],
                                  [7, 9],
                                  [11, 29],
                                  [15, 13]] )

    def aimFunc(self, pop):
        x = pop.Phen

        X = np.hstack ( [np.zeros ( (x.shape[0], 1) ), x, np.zeros ( (x.shape[0], 1) )] ).astype ( int )

        ObjV = []  # Store the total distance corresponding to all population individuals
        for i in range ( X.shape[0] ):
            journey = self.places[X[i], :]  # Coordinates of locations arriving in the established order
            distance = np.sum ( np.sqrt ( np.sum ( np.diff ( journey.T ) ** 2, 0 ) ) )  # Calculate the total distance
            ObjV.append ( distance )
        pop.ObjV = np.array ( [ObjV] ).T
        # Assign the obtained objective function value to ObjV of population pop