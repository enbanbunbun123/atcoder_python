def Infinite_coins(N, A):
    number = N % 500

    if number <= A:
        return "Yes"
    
    return "No"

N = int(input())
A = int(input())

result = Infinite_coins(N, A)
print(result)