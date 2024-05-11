def find_tallest_position(N, heights):
    tallest_index = -1
    tallest_height = 0

    for i, height in enumerate(heights):
        if height > heights[0]:
            return i + 1
    return -1

n = int(input())
heights = list(map(int, input().split()))

print(find_tallest_position(n, heights))