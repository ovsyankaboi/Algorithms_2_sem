def build_parentheses(s, i, j):
    if i == j:
        return "A"
    k = s[i][j]
    return "(" + build_parentheses(s, i, k) + build_parentheses(s, k + 1, j) + ")"

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        n_line = fin.readline()
        while n_line and n_line.strip() == '':
            n_line = fin.readline()
        n = int(n_line)

        p = []
        if n >= 1:
            a, b = map(int, fin.readline().split())
            p = [a, b]
            for _ in range(1, n):
                a, b = map(int, fin.readline().split())
                p.append(b)

    if n == 1:
        ans = "A"
    else:
        # DP-таблицы m — минимальная стоимость, s — место разреза
        m = [[0] * n for _ in range(n)]
        s = [[0] * n for _ in range(n)]

        # L — длина цепочки
        for L in range(2, n + 1):
            for i in range(0, n - L + 1):
                j = i + L - 1
                best = 10**18
                best_k = i
                # перебор разреза
                for k in range(i, j):
                    cost = (m[i][k] +
                            m[k + 1][j] +
                            p[i] * p[k + 1] * p[j + 1])
                    if cost < best:
                        best = cost
                        best_k = k
                m[i][j] = best
                s[i][j] = best_k

        ans = build_parentheses(s, 0, n - 1)

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(ans)

if __name__ == "__main__":
    solve()
