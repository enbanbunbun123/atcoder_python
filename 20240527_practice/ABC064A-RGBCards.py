def confirm_rgb_cards(r, g, b):
    number  = 100 * r + 10 * g + b

    if number % 4 == 0:
        return "YES"
    
    return "NO"

r, g, b = map(int, input().split())

result = confirm_rgb_cards(r, g, b)
print(result)