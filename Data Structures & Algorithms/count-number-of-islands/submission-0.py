from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        islands = 0

        def bfs(start):
            queue = deque([start])
            visited.add(start)


            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs((i, j))
                    islands +=1

        return islands

        


        
                

                    

        