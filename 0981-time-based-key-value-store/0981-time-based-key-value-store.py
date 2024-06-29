class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) 


    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.time_map:
            self.time_map[key] = []

        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map:
            return ''
        
        values = self.time_map[key]
        left = 0
        right = len(values) - 1
        res = ''

        while left <= right:
            mid = (left+right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)