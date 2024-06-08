def sanitizeHands(N, M, H):
    total_hands = 0

    for i in range(N):
        total_hands += H[i]

        if total_hands > M:
            return i
        
    return N

N, M = map(int, input().split())
H = list(map(int, input().split()))

result = sanitizeHands(N, M, H)
print(result)