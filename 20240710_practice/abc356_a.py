N, L, R = map(int, input().split())

L -= 1
A = list(range(1, N + 1))

result = A[:L]
result.extend(reversed(A[L:R]))
result.extend(A[R:])

print(*result)