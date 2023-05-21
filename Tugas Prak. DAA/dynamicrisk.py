def optimize_portfolio(returns, risks, target_return):
    n = len(returns)
    target_return = int(target_return * 100)  # Konversi target_return ke integer

    # Membuat matriks DP untuk menyimpan hasil optimal
    dp = [[0 for _ in range(target_return + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, target_return + 1):
            # Jika return dari aset ke-i lebih kecil dari target return
            # Ambil maksimum antara hasil dengan aset ke-(i-1)
            if int(returns[i - 1] * 100) <= j:
                dp[i][j] = max(int(risks[i - 1] * 100) + dp[i - 1][j - int(returns[i - 1] * 100)], dp[i - 1][j])
            else:
                # Jika return dari aset ke-i lebih besar dari target return
                # Ambil hasil dari aset ke-(i-1)
                dp[i][j] = dp[i - 1][j]

    # Mencari alokasi optimal dari portofolio investasi
    allocation = []
    r = target_return
    for i in range(n, 0, -1):
        if dp[i][r] != dp[i - 1][r]:
            allocation.append(i - 1)
            r -= int(returns[i - 1] * 100)

    return allocation[::-1]


# Contoh penggunaan
returns = [0.1, 0.2, 0.15, 0.18, 0.12]
risks = [0.05, 0.07, 0.03, 0.08, 0.06]
target_return = 0.3

allocation = optimize_portfolio(returns, risks, target_return)

print("Alokasi optimal dari portofolio investasi:")
for i in allocation:
    print(f"Aset {i + 1}")