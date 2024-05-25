def find_culprit(A, B):
    suspects = {1,2,3}

    suspects.discard(A)
    suspects.discard(B)

    if len(suspects) == 1:
        return suspects.pop()
    else:
        return -1
    
A, B = map(int, input().split())

result = find_culprit(A, B)
print(result)