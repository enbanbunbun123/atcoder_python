def i18n(S):
    return S[0] + str(len(S) - 2) + S[-1]

S = input()

result = i18n(S)
print(result)