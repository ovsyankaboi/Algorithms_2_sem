def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        n, W = map(int, fin.readline().split())
        items = []
        zero_weight_value = 0.0

        for _ in range(n):
            p, w = map(int, fin.readline().split())
            if w == 0:
                if p > 0:
                    zero_weight_value += float(p)
            else:
                items.append((p, w, p / w))

    items.sort(key=lambda x: x[2], reverse=True)

    total_value = zero_weight_value
    capacity = float(W)

    for p, w, d in items:
        if capacity <= 0:
            break
        take = min(capacity, float(w))
        total_value += d * take
        capacity -= take

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(f"{total_value:.4f}")

if __name__ == "__main__":
    solve()
