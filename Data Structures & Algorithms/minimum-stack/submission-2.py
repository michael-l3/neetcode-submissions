import heapq
class MinStack:

    def __init__(self):
        self.stk = [] 
        self.heap = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        heapq.heappush(self.heap,val)

    def pop(self) -> None:
        val = self.stk.pop() 
        self.heap.remove(val)
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.heap[0]
