def duplex_printing(N):
    number = N // 2
    if N % 2 == 0:
        return number
    else:
        return number + 1
    
N = int(input())

result = duplex_printing(N)
print(result)