import sys
import utils

def findNearestPoint(points, used, src):
    # If no nearest point, return max.
    dest = src
    minDist = sys.float_info.max
    i = (src + 1) % len(points)
    for j in range(len(points) - 1):
        if not used[i]:
            dist = utils.length(points[src], points[i]) 
            if dist < minDist:
                dest = i
                minDist = dist 
        i = (i + 1) % len(points)
    return dest, minDist
    
def solve(points):
    tour = [0 for i in range(len(points))]
    used = [False for i in range(len(points))]
    totalDist = 0.0
    used[0] = True
    src = 0
    for i in range(1, len(points)):
        dest, minDist = findNearestPoint(points, used, src)
        tour[i] = dest
        used[dest] = True
        src = dest
        totalDist += minDist
    return 0, totalDist + utils.length(points[tour[-1]], points[tour[0]]), tour
