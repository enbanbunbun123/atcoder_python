def find_integer_sequence(N, intervals):
    min_sum = sum(L for L, R in intervals)
    max_sum = sum(R for L, R in intervals)

    if min_sum > 0 or max_sum < 0:
        return "No"
    
    X = [L for L, R in intervals]
    current_sum = min_sum

    for i in range(N):
        L, R = intervals[i]

        if current_sum < 0:
            increase = min(R - L, -current_sum)
            X[i] += increase
            current_sum += increase
    
    return "Yes\n" + " ".join(map(str, X))

N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

print(find_integer_sequence(N, intervals))