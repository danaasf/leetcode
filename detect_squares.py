from collections import defaultdict
from typing import List

# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
class DetectSquares:

    def __init__(self):
        self.x_y = defaultdict(set)
        self.y_x = defaultdict()
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        if x in self.x_y :
            if  y not in self.x_y[x]:
                self.x_y[x].append(y)
        else:
            self.x_y[x] = [y]
        if y in self.y_x:
            if x not in self.y_x[y]:
                self.y_x[y].append(x)
        else:
            self.y_x[y] = [x]

        if (x,y) in self.points:
            self.points[(x,y)]+=1
        else: 
            self.points[(x,y)]=1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        count = 0
        
        if (x not in self.x_y) or (y not in self.y_x):
            return count
        for val_y in sorted(self.x_y[x]):
            if val_y == y:
                continue
            dist = abs(y-val_y)
            if x-dist in self.x_y and (x-dist,y) in self.points:
                val_x= x-dist
                if (val_x,val_y) in self.points:
                    count+= self.points[(val_x,y)] * self.points[(x,val_y)]*self.points[(val_x,val_y)]

            if x+dist in self.x_y and (x+dist,y) in self.points:
                val_x= x+dist
                if (val_x,val_y) in self.points:
                    count+= self.points[(val_x,y)] * self.points[(x,val_y)]*self.points[(val_x,val_y)]

        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
