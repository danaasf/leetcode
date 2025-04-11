# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0]*target
        for i in range(len(position)):
            time[position[i]] = (target-position[i])/speed[i]

        fleet = len(position)
        fast = time[max(position)]

        time =  [x for x in time if x != 0]
        for i in range(len(time)-2,-1,-1):
            if time[i]<=fast:
                fleet -=1
                fast= max(fast,time[i])
            else:
                fast=time[i]
        
        return fleet

        