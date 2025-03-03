
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
class TimeMap:

    from collections import OrderedDict

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map: 
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key]=[]
            self.time_map[key].append((timestamp, value))
        
        #time_map = OrderedDict(sorted(time_map.items(), key=lambda item: item[1]))

        

    def get(self, key: str, timestamp: int) -> str:

        if not key in self.time_map:
            return ""
        else: 
            pairs = self.time_map[key]
            left, right = 0, len(pairs) - 1
            best_value = ""

            while left<=right: 
                mid = (left+right) // 2
                if pairs[mid][0] == timestamp: 
                    best_value = pairs[mid][1]
                    return best_value 
                elif pairs[mid][0] < timestamp:
                    left = mid+1
                    best_value= pairs[mid][1]
                else:
                    right= mid-1

            
            return best_value
            



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)