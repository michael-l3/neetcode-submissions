class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #we are going to create a trie and put our desired words in it 
        #iterate through the graph to see if the letter is in it 
        #then dfs each place and if we get our word we append it to res 
        #so the end of our trie should just be the word 
        #then we can del that key after we hit it so we dont get dupes

        #we need to add the characters in the trie prior
        trie = {}
        for word in words: 
            node = trie
            for ch in word: 
                if ch not in node: 
                    node[ch] = {}
                node = node[ch]
            node['#'] = word  
        
        m = len(board)
        n = len(board[0])
        res = []

        #create the function to dfs through the grid and find the words 
        def dfs(i,j,parent_node): 
            ch = board[i][j]
            curr_node = parent_node[ch]

            #base case to append the word to the result array 
            if '#' in curr_node: 
                res.append(curr_node['#'])
                #delete it afterwarads 
                del curr_node['#']
            
            #so if we visited this area now we have to change the value of it so we dont get it again
            board[i][j] = '#'

            #now we have to check the characters around it 
            for i_off, j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                r = i + i_off 
                c = j + j_off 

                if 0 <= r < m and 0 <= c < n and board[r][c] in curr_node: 
                    dfs(r,c,curr_node) 
            
            #now if it isnt correct then we have to return the baord back to normal 
            board[i][j] = ch 

        #so we added the desired words to the trie now we have to iterate through them
        for i in range(m): 
            for j in range(n): 
                if board[i][j] in trie: 
                    dfs(i,j,trie)

        return res  


