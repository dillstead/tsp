import utils

class Opt:
    def __init__(self, points, tour, dist):
        self.points = points
        self.tour = tour
        self.endDist = dist
        
    def mapIndex(self, i):
        return i
    
    def getEndDist(self):
        return self.endDist
    
    def swap(self):
        return self.tour
        
class TwoOpt(Opt):
    def __init__(self, parent, start, end):
        self.parent = parent
        self.points = parent.points
        self.tour = parent.tour
        self.start = start
        self.end = end
        self.endDist = self.calcEndDist()
        
    def mapIndex(self, i):
        i = self.parent.mapIndex(i)
        if self.start <= i and i <= self.end:
            return self.end - (i - self.start)
        else:
            return i
        
    def getEndDist(self):
        return self.endDist
    
    def calcEndDist(self):
        # Return the new tour distance if 2opt swap is performed at start, end.
        # In the new tour, the previous point will connect to the end and the start will
        # connect to the next point.
        endDist = self.parent.getEndDist()
        oldStartEdgeLen = utils.length(self.points[self.tour[self.parent.mapIndex(self.start - 1)]], self.points[self.tour[self.parent.mapIndex(self.start)]])
        oldEndEdgeLen = utils.length(self.points[self.tour[self.parent.mapIndex(self.end)]], self.points[self.tour[self.parent.mapIndex((self.end + 1) % len(self.tour))]])
        newStartEdgeLen = utils.length(self.points[self.tour[self.parent.mapIndex(self.start - 1)]], self.points[self.tour[self.parent.mapIndex(self.end)]])
        newEndEdgeLen = utils.length(self.points[self.tour[self.parent.mapIndex(self.start)]], self.points[self.tour[self.parent.mapIndex((self.end + 1) % len(self.tour))]])
        return endDist + (newStartEdgeLen - oldStartEdgeLen) + (newEndEdgeLen - oldEndEdgeLen)

    def swap(self):
        self.tour = self.parent.swap()
        # Do the 2opt swap at start, end.
        si, ei = self.start, self.end
        while si < ei:
            self.tour[si], self.tour[ei] = self.tour[ei], self.tour[si]
            si += 1
            ei -= 1
        return self.tour
        