def apply(op: str, a: int, b: int) -> int:
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    return a * b

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        s = fin.read().strip().replace(' ', '')

    if not s:
        ans = 0
    elif len(s) == 1:
        ans = int(s)
    else:
        nums = [int(s[i]) for i in range(0, len(s), 2)]
        ops  = [s[i] for i in range(1, len(s), 2)]
        m = len(nums)

        INF = 10**18
        dp_min = [[0]*m for _ in range(m)]
        dp_max = [[0]*m for _ in range(m)]
        for i in range(m):
            dp_min[i][i] = dp_max[i][i] = nums[i]

        for L in range(2, m+1):
            for i in range(0, m-L+1):
                j = i + L - 1
                mn, mx = INF, -INF
                for k in range(i, j):
                    op = ops[k]
                    a1, a2 = dp_min[i][k], dp_max[i][k]
                    b1, b2 = dp_min[k+1][j], dp_max[k+1][j]
                    candidates = (
                        apply(op, a1, b1),
                        apply(op, a1, b2),
                        apply(op, a2, b1),
                        apply(op, a2, b2),
                    )
                    mn = min(mn, *candidates)
                    mx = max(mx, *candidates)
                dp_min[i][j] = mn
                dp_max[i][j] = mx

        ans = dp_max[0][m-1]

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(ans))

if __name__ == "__main__":
    solve()
