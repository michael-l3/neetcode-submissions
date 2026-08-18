class WordDictionary:

    def __init__(self):
        #initialize the trie 
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

        #going to have to do dfs in order to iterate through the trie 

        def dfs(index, parent_node): 
            #base case if index = len(word)
            if index == len(word): 
                return "#" in parent_node

            ch = word[index]
            #to conditions a wild card condition and a regualr condition 
            if ch == '.': 
                #checking the children in the parent node
                for child in parent_node: 
                    if child != '#' and dfs(index + 1,parent_node[child]): 
                        return True 
                return False 
            else: 
                if ch not in parent_node: 
                    return False 
                return dfs(index+1,parent_node[ch])
        
        return dfs(0,d)

