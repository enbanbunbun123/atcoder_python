def check_strings(S, T):
    if S == "AtCoder" and T == "Land":
        return "Yes"
    return "No"

S,T = input().split()

result = check_strings(S, T)
print(result)