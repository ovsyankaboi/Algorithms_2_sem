from collections import deque

def bfs(grid, qx, qy):
    n, m = len(grid), len(grid[0])
    INF = 10**9
    dist = [[INF] * m for _ in range(n)]
    if grid[qx][qy] == '1':
        return dist
    dq = deque([(qx, qy)])
    dist[qx][qy] = 0
    while dq:
        x, y = dq.popleft()
        d = dist[x][y] + 1
        for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '0' and dist[nx][ny] > d:
                dist[nx][ny] = d
                dq.append((nx, ny))
    return dist

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        N, M = map(int, fin.readline().split())
        grid = [fin.readline().strip() for _ in range(N)]

        Qx, Qy, L = map(int, fin.readline().split())  # 1-based
        musk = []
        for _ in range(4):
            line = fin.readline()
            while line is not None and line.strip() == '':
                line = fin.readline()
            if not line:
                break
            ax, ay, p = map(int, line.split())
            musk.append((ax, ay, p))

    dist = bfs(grid, Qx - 1, Qy - 1)

    total = 0
    n, m = N, M
    for ax, ay, p in musk:
        x, y = ax - 1, ay - 1
        if 0 <= x < n and 0 <= y < m and grid[x][y] == '0' and dist[x][y] <= L:
            total += p

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(total))

if __name__ == "__main__":
    solve()
