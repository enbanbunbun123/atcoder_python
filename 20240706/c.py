def solve(N, K, A):
    A.sort() 
    min_diff = float('inf')
    
    for i in range(N - (N-K) + 1):
        min_diff = min(min_diff, A[i + (N-K) - 1] - A[i])
    
    return min_diff

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve(N, K, A))