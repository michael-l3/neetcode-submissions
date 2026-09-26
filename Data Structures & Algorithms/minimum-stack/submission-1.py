class MinStack:

    def __init__(self):
        self.heap = [] 
        self.stk = []

    def push(self, val: int) -> None:
        heapq.heappush(self.heap,val)
        self.stk.append(val)

    def pop(self) -> None:
        val = self.stk.pop() 

        self.heap.remove(val)
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.heap[0]
