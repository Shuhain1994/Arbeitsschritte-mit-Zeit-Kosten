import geatpy as ea
from MyProblem import MyProblem
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    problem = MyProblem()
    Encoding = 'BG'
    NIND = 25
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) #
    population = ea.Population(Encoding, Field, NIND)
    """===============================Algorithm parameter settings============================="""
    myAlgorithm = ea.moea_NSGA3_templet(problem, population)
    myAlgorithm.MAXGEN = 25
    myAlgorithm.drawing = 0
    """==========================Call algorithm template for population evolution======================="""
    NDSet = myAlgorithm.run()
    NDSet.save()
    # output
    print ( 'Seconds: %s' % (myAlgorithm.passTime) )
    print ( 'Non-dominated individuals：%s ' % (NDSet.sizes) )
    print ( 'Decision variable value：%s ' % (NDSet.Phen) )
    print ( 'Decision target value：%s ' % (NDSet.ObjV) )

fig, axs = plt.subplots (3,1)

x = np.arange(0,8)
y1 = NDSet.Phen[-1,:]

y2 = y1.copy()
y2[y1==0]=2
y2[y1==1]=3
y2[y1==2]=4

y3 =y2.copy()
y3[y2==3]=2
y3[y2==2]=3


axs[2].step(x, y3, where='post', color='red')
axs[2].set_title('Kosten für jeden Schritt', size= 14)
axs[2].grid(axis='x', color='0.95')
axs[2].plot(x, y3, 'o--', color='grey', alpha=0.3)

axs[1].step(x, y2, where='post', color='blue')
axs[1].set_title('Zeit für jeden Schritt', size= 14)
axs[1].grid(axis='x', color='0.95')
axs[1].plot(x, y2, 'o--', color='grey', alpha=0.3)

axs[0].step(x, y1, where='post', color='orange')
axs[0].set_title('Fertigungsschritte', size= 14)
axs[0].grid(axis='x', color='0.95')
axs[0].plot(x, y1, 'o--', color='grey', alpha=0.3)

fig.tight_layout()
plt.show()