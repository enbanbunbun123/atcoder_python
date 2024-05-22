def canconstruct_from_suffixes(S):
    suffixes = ['dream', 'dreamer', 'erase', 'eraser']

    #Sを後ろから見ているgreedyアルゴリズム
    S = S[::-1]
    suffixes = [suffix[::-1] for suffix in suffixes]

    i = 0
    while i < len(S):
        matched = False
        for suffix in suffixes:
            if S[i:i+len(suffix)] == suffix:
                matched = True
                i += len(suffix)
                break
        
        if not matched:
            return "NO"
    return "YES"
    
S = input().strip()

print(canconstruct_from_suffixes(S))