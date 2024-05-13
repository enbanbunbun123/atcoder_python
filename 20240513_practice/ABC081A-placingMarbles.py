def placingMarbles(numbers):
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == 1:
            count += 1
    
    return count

numbers = list(map(int, input().strip()))

print(placingMarbles(numbers))