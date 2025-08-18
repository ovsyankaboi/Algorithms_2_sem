import sys
sys.setrecursionlimit(1 << 20)

def solve():
    lines = [ln.rstrip('\n') for ln in open('input.txt', 'r', encoding='utf-8')]
    it = iter(lines)
    n = int(next(it))

    names, calls = [], []
    for _ in range(n):
        name = next(it).strip()
        names.append(name)
        k = int(next(it))
        calls.append([next(it).strip() for __ in range(k)])
        _ = next(it)

    idx = {name: i for i, name in enumerate(names)}
    g  = [[] for _ in range(n)]
    gt = [[] for _ in range(n)]
    selfloop = [False]*n

    for u in range(n):
        for nm in calls[u]:
            v = idx[nm]
            g[u].append(v)
            gt[v].append(u)
            if v == u:
                selfloop[u] = True

    used, order = [False]*n, []
    def dfs(v):
        used[v] = True
        for w in g[v]:
            if not used[w]: dfs(w)
        order.append(v)

    for v in range(n):
        if not used[v]: dfs(v)

    comp = [-1]*n; cid = 0
    def rdfs(v, cid):
        comp[v] = cid
        for w in gt[v]:
            if comp[w] == -1: rdfs(w, cid)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid); cid += 1

    sz = [0]*cid
    for v in range(n): sz[comp[v]] += 1

    ans = ["YES" if (sz[comp[v]] > 1 or selfloop[v]) else "NO" for v in range(n)]
    open('output.txt', 'w', encoding='utf-8').write("\n".join(ans))

if __name__ == "__main__":
    solve()
