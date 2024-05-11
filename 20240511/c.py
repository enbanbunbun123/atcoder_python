def f(x,y):
    return (x + y) % (10**8)

n = int(input())
a = list(map(int, input().split()))

result = 0
for i in range(n-1):
    for j in range(i+1, n):
        result += f(a[i], a[j])

print(result)
