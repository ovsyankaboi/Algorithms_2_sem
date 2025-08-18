from collections import deque
def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        data = list(map(int, fin.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)

    outs = [[] for _ in range(n + 1)]
    ins  = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        outs[u].append(v)
        ins[v].append(u)

    INF = 10**9
    answer = 0

    for s in range(1, n + 1):
        dist = [INF] * (n + 1)
        dist[s] = 0
        dq = deque([s])

        while dq:
            u = dq.popleft()
            du = dist[u]

            for v in outs[u]:
                if dist[v] > du:
                    dist[v] = du
                    dq.appendleft(v)
            for v in ins[u]:
                if dist[v] > du + 1:
                    dist[v] = du + 1
                    dq.append(v)
        local_max = 0
        for i in range(1, n + 1):
            if dist[i] > local_max:
                local_max = dist[i]
        if local_max > answer:
            answer = local_max

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(answer))

if __name__ == "__main__":
    solve()
