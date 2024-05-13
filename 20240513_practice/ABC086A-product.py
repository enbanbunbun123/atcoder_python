def classify_odd(numbers):
    product = numbers[0] * numbers[1]

    if product % 2 == 0:
        return "Even"
    else:
        return "Odd"

numbers = list(map(int, input().split()))

print(classify_odd(numbers))
