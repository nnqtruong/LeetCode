from collections import defaultdict

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        max_score = -1
        # Step 2: Pre-compute top 3 neighbors for each node
        top3 = {}
            # Sort neighbors by their scores (descending)
        for node in graph:
            neighbors = sorted(graph[node], key=lambda x: scores[x], reverse = True)
            top3[node] = neighbors[:3]
        

        # Step 3: For each edge as middle edge
        for u, v in edges:
            # Only check top 3 neighbors of u and v
            for node1 in top3[u]:
                if node1 == v:
                    continue
                for node4 in top3[v]:
            # Skip if it's the other middle node
                    if node4 ==u or node4 == node1:
                        continue
                    score = scores[node1] + scores[node4] + scores[u] + scores[v]
                    max_score = max(max_score,score)
        return max_score
            # All must be distinct