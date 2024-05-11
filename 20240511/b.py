def identify_menbers(N, K, groups):
    empty_seats = K
    start_count = 0
    i = 0

    while i < N:
        if empty_seats >= groups[i]:
            empty_seats -= groups[i]
            i += 1
        else:
            empty_seats = K
            start_count += 1

    if empty_seats < K:
        start_count += 1
    
    return start_count

n, k = map(int, input().split())
groups = list(map(int, input().split()))

print(identify_menbers(n, k, groups))