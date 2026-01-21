class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        m,n = len(grid),len(grid[0])
        start_r,start_c= 0,0
        all_keys = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '@':
                    start_r,start_c = r,c
                elif grid[r][c].islower():
                    all_keys |= (1 <<(ord(grid[r][c]) - ord('a')))

        #BFS
        queue = deque([(start_r,start_c,0,0)])
        visited = {(start_r,start_c,0)}

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while queue:
            r,c,keys,steps = queue.popleft()

            #goal check
            if keys == all_keys:
                return steps

            #Try 4 directions
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                #Bounds check
                if not (0<=nr < m and 0 <=nc <n):
                    continue
                cell = grid[nr][nc]

                if cell == "#":
                    continue

                new_keys = keys

                #key 
                if cell.islower():
                    new_keys   |= (1 << (ord(cell)-ord('a')))

                #Lock
                elif cell.isupper():
                    if not (keys & (1 <<(ord(cell)-ord('A')))):
                        continue
                        
                if (nr,nc,new_keys) not in visited:
                    visited.add((nr,nc,new_keys))
                    queue.append((nr,nc,new_keys,steps+1))
        return -1
