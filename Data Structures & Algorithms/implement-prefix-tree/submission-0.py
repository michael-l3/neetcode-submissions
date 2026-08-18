class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie 

        #iterate though the characters of the word 
        for ch in word: 
            #if it isnt in the trie then add it 
            if ch not in d: 
                d[ch] = {}
            #move into the next child node 
            d = d[ch]
        
        #something has to mark the end of the word --> we will use '#'
        d['#'] = True 

    def search(self, word: str) -> bool:
        #simiar to insert 
        d = self.trie 

        for ch in word: 
            if ch not in d: 
                return False 
            d = d[ch] 
        
        #signals the end of the word
        return '#' in d

    def startsWith(self, prefix: str) -> bool:
        #similar to search 
        d = self.trie 

        for ch in prefix: 
            if ch not in d: 
                return False 
            d = d[ch] 
        
        #signals the end of the word
        return True 
        