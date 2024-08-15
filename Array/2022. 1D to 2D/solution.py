class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix = []
        if m*n == len(original):
            a = 0
            for j in range(0,m):
                row = []
                for i in range(0,n):
                    row.append(original[a])
                    a +=1
                matrix.append(row)
            return matrix
        else:
            return []