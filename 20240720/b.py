N, T, P = map(int, input().split())
L = list(map(int, input().split()))

def days_until_people_have_length_T(N, T, P, L):
    count_T = sum(1 for length in L if length >= T)

    if count_T >= P:
        return 0
    
    #配列Lの中で、Tになるためには何日必要なのかを配列day_neededに格納する
    #ただし、すでにTを超えているものに関しては、無視する
    day_needed = []
    for length in L:
        if(length < T):
            day_needed.append(T - length)

    day_needed.sort()

    return day_needed[P - count_T - 1]


result = days_until_people_have_length_T(N, T, P, L)
print(result)