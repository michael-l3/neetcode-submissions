class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        #call the trie 
        d = self.trie 

        #go through all of the words in a nested form and keep going into the nested dictionary until 
        #the characters arent there and add them 
        for ch in word: 
            if ch not in d: 
                d[ch] = {} 
            
            #then enter that nested to keep going down 
            d = d[ch]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self .trie 

        for ch in word: 
            if ch not in d: 
                return False 
            d = d[ch]

        #at the end we need to make sure the word is there by returning the '.' 
        return '.' in d
        

    def startsWith(self, prefix: str) -> bool:
        d = self .trie 

        for ch in prefix: 
            if ch not in d: 
                return False 
            d = d[ch]

        #at the end we need to make sure the word is there by returning the '.' 
        return True
        
        