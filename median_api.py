import heapq


class MedianFinder:

    def __init__(self):
        #two heaps, max heap for smaller vals and min heap for larger vals
        self.max_heap , self.min_heap = [] , []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-1 * num)
        #we have to make sure every element in max heap is smaller than every element in min heap
        #we also have to make sure the size difference of the heap is at most 1 
        if (self.max_heap and self.min_heap and (-1 * self.max_heap[0]) > self.min_heap[0] ): #max_heap[0] is the max val
            # we have to pop from max_heap and add to min_heap
            element = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, element)
        
        if len(self.max_heap) > len(self.min_heap)+1 :
            element = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, element)

        if  len(self.min_heap) > len(self.max_heap)+1 :
            element = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * element)


    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0] 
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-1 * self.max_heap[0]+ self.min_heap[0] )/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()