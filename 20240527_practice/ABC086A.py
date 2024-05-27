def check_odd_even(a, b):
    if (a * b) % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
a, b = map(int, input().split())

result = check_odd_even(a, b)
print(result)