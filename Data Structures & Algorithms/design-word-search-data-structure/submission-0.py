class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie 

        for ch in word: 
            if ch not in d: 
                d[ch] = {}
            d = d[ch]
        
        d['#'] = True 


    def search(self, word: str) -> bool:
        d = self.trie 

        def dfs(index, parent_node): 
            
            if index == len(word): 
                return '#' in parent_node 
            
            ch = word[index]

            if ch == '.': 
                #then we have a wildcard and can enter the childen bc this one doesnt matter it can be anything 
                for child in parent_node: 
                    if child != '#' and dfs(index+1,parent_node[child]): 
                        return True 
                return False 
            else: 
                if ch not in parent_node: 
                    return False 
                return dfs(index+1,parent_node[ch])
        
        return dfs(0,d)
        
