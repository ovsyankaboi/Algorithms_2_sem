MOD = 10 ** 9

MOVES = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        n_line = fin.read().strip()
    N = int(n_line)

    # База длина 1 — нельзя начинать с 0 и 8
    dp = [0] * 10
    for d in [1, 2, 3, 4, 5, 6, 7, 9]:
        dp[d] = 1

    for _ in range(2, N + 1):
        nxt = [0] * 10
        for d in range(10):
            if dp[d] == 0:
                continue
            for t in MOVES[d]:
                nxt[t] = (nxt[t] + dp[d]) % MOD
        dp = nxt

    ans = sum(dp) % MOD if N >= 1 else 0

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(ans))

if __name__ == "__main__":
    solve()
