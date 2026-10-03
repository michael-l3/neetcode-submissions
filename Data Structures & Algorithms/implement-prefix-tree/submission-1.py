class PrefixTree:

    def __init__(self):
        #a trie is a dictionary of dictionaries 
        self.trie = {}
    def insert(self, word: str) -> None:
        t = self.trie

        for ch in word: 
            if ch not in t: 
                t[ch] = {}
                #then we move into int 
            t = t[ch]
        t['.'] = '.'

    def search(self, word: str) -> bool:
        t = self.trie

        for ch in word: 
            if ch not in t: 
                return False
                #then we move into int 
            t = t[ch]
        return '.' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie

        for ch in prefix: 
            if ch not in t: 
                return False
                #then we move into int 
            t = t[ch]
        return True
        