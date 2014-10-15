import time
import utils
import fpformat
from opt import Opt, TwoOpt 

maxTimeToRun = 60 * 60 * 4

# TODO:
# Possible improvements:
#  1) cache distance calculations in TwoOpt
#  2) only perform the shorter swap 
#  3) cache distances between two points

def getBestThreeOpt(points, tour, currentDist, i, j, k):
    # Find the best 3-opt sequence out of the 7 possibilities.
    # The first 3 possibilities are 2-opts.
    #  A -> B x C -> D x E -> F -> G -> H
    twoOpt1 = TwoOpt(Opt(points, tour, currentDist), i, j)
    bestThreeOptSequence = twoOpt1
    #  A -> B -> C -> D x E x F -> G -> H
    twoOpt2 = TwoOpt(Opt(points, tour, currentDist), j + 1, k)
    if twoOpt2.getEndDist() < bestThreeOptSequence.getEndDist():
        bestThreeOptSequence = twoOpt2
    #  A -> B x C -> D -> E x F -> G -> H
    twoOpt3 = TwoOpt(Opt(points, tour, currentDist), i, k)
    if twoOpt3.getEndDist() < bestThreeOptSequence.getEndDist():
        bestThreeOptSequence = twoOpt3
    # The next 3 possibilities are sequences of 2 2-opts.
    doubleTwoOpt1 = TwoOpt(twoOpt1, j + 1, k)
    if doubleTwoOpt1.getEndDist() < bestThreeOptSequence.getEndDist():
        bestThreeOptSequence = doubleTwoOpt1
    doubleTwoOpt2 = TwoOpt(twoOpt3, i, j)
    if doubleTwoOpt2.getEndDist() < bestThreeOptSequence.getEndDist():
        bestThreeOptSequence = doubleTwoOpt2
    doubleTwoOpt3 = TwoOpt(twoOpt3, j + 1, k)
    if doubleTwoOpt3.getEndDist() < bestThreeOptSequence.getEndDist():
        bestThreeOptSequence = doubleTwoOpt3
    # The final possibility is a sequence of 3 2-opts.
    tripleTwoOpt1 = TwoOpt(doubleTwoOpt1, i, k)
    if tripleTwoOpt1.getEndDist() < bestThreeOptSequence.getEndDist():
        bestThreeOptSequence = tripleTwoOpt1
    return bestThreeOptSequence

def solve(points, tour, currentDist):
    startTime = int(time.time())
    print("points: " + str(len(tour)) + " start tour" + str(tour))
    step = 0
    offset = lambda x: 1 if x == 1 else 0
    while True:
        # The best opt and distance.
        startStepTime = int(time.time())
        bestDist = currentDist
        bestThreeOpt = None
        tries = 0
        for i in range(1, len(tour) - 3):  
            for j in range(i + 1, len(tour) - 2):
                for k in range(j + 2, len(tour) - offset(i)):
                    #print("i: %d, j: %d, j+1: %d, k:%d" % (i, j, j +1, k))
                    tries += 1 
                    threeOpt = getBestThreeOpt(points, tour, currentDist, i, j, k)
                    if threeOpt.getEndDist() < bestDist:
                        bestDist = threeOpt.getEndDist()
                        bestThreeOpt = threeOpt
        step += 1
        utils.dprint("step: " + str(step) + ", tries: " + str(tries) + ", time: " + fpformat.fix(time.time() - startStepTime, 3))
        if bestDist == currentDist:
            # If no more improvement we are at a local minima and are done.
            print("no more improvement")
            break
        # Perform the opt.
        bestThreeOpt.swap();
        currentDist = bestDist
        if  int(time.time()) - startTime > maxTimeToRun:
            # Out of time, return the best we've got.
            print("out of time")
            break
    print("end tour" + str(tour))
    return 0, bestDist, tour
