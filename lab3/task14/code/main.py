def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        tokens = fin.read().split()
    it = iter(tokens)
    n = int(next(it))
    d = int(next(it))
    v = int(next(it))
    r = int(next(it))

    trips = []
    for _ in range(r):
        u = int(next(it))
        t_dep = int(next(it))
        w = int(next(it))
        t_arr = int(next(it))
        trips.append((t_dep, u, w, t_arr))

    trips.sort(key=lambda x: x[0])

    INF = 10**15
    earliest = [INF] * (n + 1)
    earliest[d] = 0

    for t_dep, u, w, t_arr in trips:
        if earliest[u] <= t_dep and t_arr < earliest[w]:
            earliest[w] = t_arr

    ans = earliest[v] if earliest[v] < INF else -1

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(ans))

if __name__ == "__main__":
    solve()

