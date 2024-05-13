def shift_only(numbers):
    # 与えられた数列の中に奇数がある時には0を返す
    for num in numbers:
        if num % 2 != 0:
            return 0
        
    # 与えられた数列が何回和rことができるかどうかをカウントする
    count = 0
    while all(num % 2 == 0 for num in numbers):
        numbers = [num // 2 for num in numbers]
        count += 1
        
    return count

N = int(input())
numbers = list(map(int, input().split()))

print(shift_only(numbers))