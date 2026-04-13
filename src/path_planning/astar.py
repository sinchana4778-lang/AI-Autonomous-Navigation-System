import heapq

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    def heuristic(a, b):
      return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        r, c = current

        # 🔥 STRICT ROW, COL MOVEMENT
        neighbors = [
          (r, c + 1),   # right
          (r + 1, c),   # down
          (r, c - 1),   # left
          (r - 1, c)    # up
]

        for nr, nc in neighbors:
            # bounds
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            # obstacle
            if grid[nr][nc] == 1:
                continue

            temp_g = g_score[current] + 1

            if (nr, nc) not in g_score or temp_g < g_score[(nr, nc)]:
                g_score[(nr, nc)] = temp_g
                f = temp_g + heuristic((nr, nc), goal)
                heapq.heappush(open_set, (f, (nr, nc)))
                came_from[(nr, nc)] = current

    return []