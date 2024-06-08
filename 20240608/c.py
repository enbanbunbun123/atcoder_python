def generate_carpet(N):
    size = 3 ** N
    carpet = [['#'] * size for _ in range(size)]

    def fill_carpet(x, y, level):
        if level == 0:
            return
        
        block_size = 3 ** (level - 1)
        for i in range(block_size):
            for j in range(block_size):
                carpet[x + block_size + i][y + block_size + j] = '.'

        for dx in range(3):
            for dy in range(3):
                if dx != 1 or dy != 1:
                    fill_carpet(x + dx * block_size, y + dy * block_size, level - 1)

    fill_carpet(0, 0, N)
    return carpet

def print_carpet(carpet):
    for row in carpet:
        print(''.join(row))

N = int(input().strip())

result = generate_carpet(N)
print_carpet(result)