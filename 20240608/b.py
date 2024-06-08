def UppercaseAndLowercase(S):
    upper_count = sum(1 for c in S if c.isupper())
    lower_count = len(S) - upper_count

    if upper_count > lower_count:
        return S.upper()
    elif upper_count < lower_count:
        return S.lower()

S = input().strip()

result = UppercaseAndLowercase(S)
print(result)