def calculate_ramen_price(S):
    base_price = 700

    topping_price = 100

    total_price = base_price

    for chr in S:
        if chr == "o":
            total_price += topping_price


    return total_price

S = input()

result = calculate_ramen_price(S)
print(result)