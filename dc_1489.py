from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.map = {}
    def set(self, key, value, time):
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((time, value))
    def get(self, key, time):
        if key not in self.map:
            return None
        it = bisect_right(self.map[key], (time,))
        if it == 0:
            return None
        return self.map[key][it - 1][1]

d = TimeMap()
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 2)  # set key 1 to value 2 at time 2
print(d.get(1, 1))  # should print 1
print(d.get(1, 3))  # should print 2
d.set(1, 1, 5)  # set key 1 to value 1 at time 5
print(d.get(1, 0))  # should print None (no value set at time 0)
print(d.get(1, 10)) # should print 1 (value at most recent time before 10)
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 0)  # set key 1 to value 2 at same time 0
print(d.get(1, 0)) # should print 2 (most recent value at time 0)