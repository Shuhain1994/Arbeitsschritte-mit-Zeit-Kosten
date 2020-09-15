import numpy as np
import geatpy as ea
import matplotlib.pyplot as plt
from MyProblem import MyProblem

if __name__ == '__main__':
    problem = MyProblem()
    Encoding = 'P'
    NIND = 50
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)
    population = ea.Population(Encoding, Field, NIND)
    myAlgorithm = ea.soea_SEGA_templet(problem, population) #
    myAlgorithm.MAXGEN = 100
    myAlgorithm.mutOper.Pm = 0.5
    myAlgorithm.drawing = 1
    [population, obj_trace, var_trace] = myAlgorithm.run()
    population.save()

    best_gen = np.argmin(problem.maxormins * obj_trace[:, 1])
    best_ObjV = np.min(obj_trace[:, 1])
    print('Kürzeste Entfernung：%s'%(best_ObjV))
    print('Beste Route：')
    best_journey = np.hstack([0, var_trace[best_gen, :], 0])
    for i in range(len(best_journey)):
        print(chr(int(best_journey[i]) + 65), end = ' ')
    print()
    print('Anzahl der effektiven Evolutionen：%s'%(obj_trace.shape[0]))
    print('Die beste Generation ist die %s Generation'%(best_gen + 1))
    print('Anzahl der Bewertungen：%s'%(myAlgorithm.evalsNum))
    print('Zeitaufwand %s sek'%(myAlgorithm.passTime))

    plt.figure()
    plt.plot(problem.places[best_journey.astype(int), 0], problem.places[best_journey.astype(int), 1], c = 'black')
    plt.plot(problem.places[best_journey.astype(int), 0], problem.places[best_journey.astype(int), 1], 'o', c = 'black')
    for i in range(len(best_journey)):
        plt.text(problem.places[int(best_journey[i]), 0], problem.places[int(best_journey[i]), 1], chr(int(best_journey[i]) + 65), fontsize=20)
    plt.grid(True)
    plt.xlabel('x-Achse')
    plt.ylabel('y-Achse')
    plt.savefig('roadmap.svg', dpi=600, bbox_inches='tight')