class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["} 
        stk = [] 

        for ch in s: 
            if ch not in hashmap: 
                stk.append(ch)
            else:
                if not stk: 
                    return False
                else:
                    compare = stk.pop() 
                    if compare != hashmap[ch]: 
                        return False 
        
        return not stk