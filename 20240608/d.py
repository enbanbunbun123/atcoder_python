def calcurate_reminder(N):
    MOD = 998244353

    power_mod = pow(10, N, MOD)
    sum_mod = (power_mod - 1) % MOD
    inverse_9 = pow(9, MOD - 2, MOD)
    result = (sum_mod * inverse_9) % MOD
    result = (N * result) % MOD

    return result

N = int(input().strip())
print(calcurate_reminder(N))