class TimeMap:

    def __init__(self):
        self.keyHistories= {} # Key: key, Val: (timestamp, value)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        info = (timestamp, value)
        if key not in self.keyHistories:
            self.keyHistories[key] = [info]
            return

        self.keyHistories[key].append(info)



    def get(self, key: str, timestamp: int) -> str:
        # Binary search with upperbound of timestamp
        if key not in self.keyHistories:
            return ""
        history = self.keyHistories[key]

        l, r = 0, len(history) - 1
        valIndex = 0
        while l <= r:
            mid = (l+r) // 2
            time = history[mid][0]
            if time <= timestamp:
                valIndex = mid
                l = mid + 1
            else:
                r = mid - 1
        # If we never fou
        if history[valIndex][0] > timestamp:
            return ""
        
        return history[valIndex][1]

