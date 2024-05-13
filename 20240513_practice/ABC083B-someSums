def digit_sum(n):
    return sum(map(int, str(n)))

def sum_of_numbers(N, A, B):
    count = 0

    for i in range(1, N+1):
        ds = digit_sum(i)

        if A <= ds <= B:
            count += i
        
    return count

N, A, B = map(int, input().split())

print(sum_of_numbers(N, A, B))