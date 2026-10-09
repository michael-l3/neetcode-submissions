class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens: 
            if t in "+*-/": 
                if t == "+": 
                    val2 = stk.pop() 
                    val1 = stk.pop()
                    stk.append(val1 + val2)
                elif t == "-": 
                    val2 = stk.pop() 
                    val1 = stk.pop()
                    stk.append(val1 - val2)
                elif t == "*": 
                    val2 = stk.pop() 
                    val1 = stk.pop()
                    stk.append(val1 * val2)
                else: 
                    val2 = stk.pop() 
                    val1 = stk.pop()
                    d = val1 / val2 
                    stk.append(int(d))
            else: 
                stk.append(int(t))
        
        return stk[-1]