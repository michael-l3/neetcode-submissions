class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store: 
            self.store[key].append((timestamp,value))
        else: 
            self.store[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: 
            return ''
        lst = self.store[key]
        if timestamp < lst[0][0]: 
            return ''
        
        l = 0 
        r = len(lst) - 1 

        while l < r: 
            m = (l+r+1) // 2 
            m_timestamp = lst[m][0]

            if timestamp < m_timestamp: 
                r = m - 1 
            elif timestamp > m_timestamp: 
                l = m 
            else: 
                return lst[m][1]
        
        return lst[l][1]