def check_consective(N, M, A, B):
    C = sorted(A + B)

    a_set = set(A)
    for i in range(len(C) -1):
        if C[i] in a_set and C[i+1] in a_set:
            return "Yes"
    return "No"

N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = check_consective(N, M, A, B)
print(result)