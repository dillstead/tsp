import math

def outputStep(step, name, opt, bestDist, tour):
    output_data = str(bestDist) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, tour))
    ofile = open("%s-%d.out" % (name, step), "w")
    ofile.write(output_data)
    ofile.flush()

def getDist(points, tour):
    dist = 0.0
    for i in range(len(tour) - 1):
        dist += length(points[tour[i]], points[tour[i + 1]])
    dist += length(points[tour[-1]], points[tour[0]])
    return dist
    
def verifyDist(points, tour, dist):
    assert(getDist(points, tour) == dist)

def dprint(message):
    if True:
        print(message)
        
lengthCache = None   
def length(point1, point2):
    i = min(point1.idx, point2.idx)
    j = max(point1.idx, point2.idx) - (i + 1)
    if lengthCache[i][j] == 0.0:
        lengthCache[i][j] = math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    return lengthCache[i][j]