class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #building the trie for the words that we are looking for 
        trie = {} 
        for word in words: 
            node = trie 
            for ch in word: 
                if ch not in node: 
                    node[ch] = {}
                node = node[ch]
            node['#'] = word 
        

        #row 
        m = len(board)
        n = len(board[0])
        res = []

        #iterate through the board using dfs function 
        def dfs(r,c,parent_node): 
            ch = board[r][c]
            curr_node = parent_node[ch]

            #base case to append
            if '#' in curr_node: 
                res.append(curr_node['#'])
                del curr_node['#'] 
            
            #now we have to mark the current spot as a visited area 
            board[r][c] = '#'

            for r_off, c_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rx = r + r_off 
                cx = c + c_off 

                if 0 <= rx < m and 0 <= cx < n and board[rx][cx] in curr_node: 
                    dfs(rx,cx,curr_node)
            
            #if nothing returns then return the letter back to normal
            board[r][c] = ch 
        
        for i in range(m): 
            for j in range(n): 
                if board[i][j] in trie: 
                    dfs(i,j,trie)
        return res

                