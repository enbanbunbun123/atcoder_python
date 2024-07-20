from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def contains_k_length_palindrome(s, K):
    for i in range(len(s) - K + 1):
        if is_palindrome(s[i:i + K]):
            return True
    return False

def count_no_palindromic_permutations(N, K, S):
    original_permutations = set(permutations(S))
    count = 0

    for perm in original_permutations:
        perm_str = ''.join(perm)

        if not contains_k_length_palindrome(perm_str, K):
            count += 1
    
    return count

N, K = map(int, input().split())
S = input().strip()

result = count_no_palindromic_permutations(N, K, S)
print(result)

