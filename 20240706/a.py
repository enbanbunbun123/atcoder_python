N, K, X = map(int, input().split())
a = list(map(int, input().split()))

b = a[:K] + [X] + a[K:]

print(" ".join(map(str, b)))