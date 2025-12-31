from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        #define len grid and directions
        n = len(grid)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        # Step 1: Multi source BDS to compute dist to nearest thief
            # define INF distance grid to compute later size nxn
        INF = 10**9
        dist = [[INF]*n for _ in range(n)]
        q = deque()

            # Find 1s in the grid then put it in queue
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    dist[r][c] = 0
                    q.append((r,c))
        #Fill the INF grid with distance
        while q:
            r,c = q.popleft() #pop q until no more q 
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<= nr < n and 0<= nc <n and dist[nr][nc] == INF:
                    dist[nr][nc]=dist[r][c]+1
                    q.append((nr,nc))

    #Step 2: max-bottleneck path using max-heap
        #define nxn table -1 safeness level
        best = [[-1]*n for _ in range(n)]
        #safeness at 0,0 is distance from 0,0
        best[0][0]=dist[0][0]
        #python heap is min heap, use " - " before safety grid for max heap
        # heap = (current safeness, rol, col)
        heap = [(-best[0][0],0,0)]
        #Loop: best-first search
        while heap:
            s,r,c = heapq.heappop(heap)
            s=-s
        # early exit, heap pops highest safeness first
            if (r,c)==(n-1,n-1):
                return s

        #ignore worse paths
            if s < best[r][c]:
                continue

        # relax neighbors
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
        # compute new safeness
                if 0<= nr < n and 0<= nc <n:
                    ns = min(s,dist[nr][nc])

        # relexation condition
                    if ns > best[nr][nc]:
                        best[nr][nc] = ns
                        heapq.heappush(heap, (-ns, nr, nc))
        return 0

    