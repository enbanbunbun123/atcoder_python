def ticket_puchase_time(N, A, T):
    current_time = 0

    results = []

    for i in range(N):
        arrival_time = T[i]

        if current_time < arrival_time:
            current_time = arrival_time

        finish_time = current_time + A
        results.append(finish_time)
        current_time = finish_time

    return results

N, A = map(int, input().split())
T = list(map(int, input().split()))

results = ticket_puchase_time(N, A, T)

for result in results:
    print(result)