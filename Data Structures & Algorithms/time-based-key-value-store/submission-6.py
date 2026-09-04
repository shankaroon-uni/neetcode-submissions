class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        l = 0
        r = len(values)
        res = ""
        while l < r:
            m = (l + r) // 2
            tmp = values[m][0]
            value = values[m][1] 
            if timestamp >= tmp:
                res = value
                l = m + 1
            else:
                r = m
        return res
