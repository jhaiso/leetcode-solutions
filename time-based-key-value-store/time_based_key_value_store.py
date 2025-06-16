class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.keyStore:
            values = self.keyStore[key]
            l, r = 0, len(values)-1
            while l <= r:
                m = l + (r-l) // 2
                if values[m][1] > timestamp:
                    r = m - 1
                else:
                    res = values[m][0]
                    l = m + 1
            
        return res