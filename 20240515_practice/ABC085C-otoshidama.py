def find_bills_combination(N, Y):
    for i in range(N + 1):
        for j in range(N + 1 - i):
            k = N - i - j

            if 10000 * i + 5000 * j + 1000 * k == Y:
                return i, j, k
    return -1, -1, -1

N, Y = map(int,input().split())

result = find_bills_combination(N, Y)
print(result[0], result[1], result[2])