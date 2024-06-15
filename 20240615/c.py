def min_stalls_to_cover_all_tastes(N, M, stalls):
    masks = []
    for stall in stalls:
        mask = 0
        for i in range(M):
            if stall[i] == 'o':
                mask |= (1 << i)
        masks.append(mask)
    
    all_tastes = (1 << M) - 1
    
    INF = float('inf')
    dp = [INF] * (1 << M)
    dp[0] = 0

    for mask in masks:
        for prev in range((1 << M) - 1, -1, -1):
            dp[prev | mask] = min(dp[prev | mask], dp[prev] + 1)

    return dp[all_tastes]

N, M = map(int, input().split())
stalls = [input().strip() for _ in range(N)]

print(min_stalls_to_cover_all_tastes(N, M, stalls))
