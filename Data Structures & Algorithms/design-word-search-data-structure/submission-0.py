class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie 

        for ch in word: 
            if ch not in d: 
                d[ch] = {} 
            #move into it 
            d = d[ch]
        
        #because the dot is used as a wild card we want to use something else as the end of the word 
        # instead of this : d['.'] = '.', we will use this to represent the end of a word
        d['#'] = True

    def search(self, word: str) -> bool:
        d = self.trie 

        #now we will search using dfs 
        def dfs(index, dictionary):  #the index that we are currently at in the word and the starting dictionary(we are nested)
            #base case is if the index is equal to the amount of letters in the word 
            if index == len(word): 
                #make sure we are returning the last part 
                return '#' in dictionary #-> returns True if it is there False if not
            
            #finding the character now 
            ch = word[index]

            #wildCard case 
            if ch == '.': 
                #then go through all of the characters in the child nodes that exist 
                for child in dictionary: 
                    if child != '#' and dfs(index+1,dictionary[child]): 
                        return True 
                return False 
            else: 
                if ch not in dictionary: 
                    return False 
                return dfs(index+1,dictionary[ch]) 
        
        return dfs(0,d)


        
