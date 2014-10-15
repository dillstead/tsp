import utils
import time
import fpformat
from opt import Opt, TwoOpt

maxTimeToRun = 60 * 60 * 4

def solve(points, tour, currentDist):
    startTime = int(time.time())
    print("points: " + str(len(tour)) + " start tour" + str(tour))
    # 0    1    2   3
    # a -> b -> c ->d
    step = 0
    while True:
        # The best opt and distance.
        startStepTime = int(time.time())
        bestDist = currentDist
        bestTwoOpt = None
        tries = 0
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                tries += 1
                twoOpt = TwoOpt(Opt(points, tour, currentDist), i, j)
                if twoOpt.getEndDist() < bestDist:
                    bestDist = twoOpt.getEndDist()
                    bestTwoOpt = twoOpt
        step += 1
        utils.dprint("step: " + str(step) + ", tries: " + str(tries) + ", time: " + fpformat.fix(time.time() - startStepTime, 3))
        if bestDist == currentDist:
            # If no more improvement we are at a local minima and are done.
            print("no more improvement")
            break
        # Perform the opt.
        bestTwoOpt.swap();
        currentDist = bestDist
        #solver.outputStep(step, 0, bestDist, tour)
        if  int(time.time()) - startTime > maxTimeToRun:
            # Out of time, return the best we've got.
            print("out of time")
            break
        step += 1
    print("end tour" + str(tour))
    return 0, bestDist, tour
