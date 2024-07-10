def twoAnagrams(s, t):
    sorted_s = '.'.join(sorted(s))
    sorted_t = '.'.join(sorted(t))

    if sorted_s < sorted_t:
        return 'Yes'
    return 'No'

s = input()
t = input()

result = twoAnagrams(s, t)
print(result)