def culcurate_kagami_mochi(N, diameters):
    diameters = sorted(set(diameters), reverse=True)

    return len(diameters)


N = int(input())
diameters = [int(input()) for _ in range(N)]

print(culcurate_kagami_mochi(N, diameters))