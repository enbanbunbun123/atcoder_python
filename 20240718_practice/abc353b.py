N, K = map(int, input().split())
A = list(map(int, input().split()))

left = K
count = 0

for a in A:
    #残り席数が人数よりも少ない時に、次の回に乗車し発射回数を１つ増やす
    if left < a:
        count += 1
        left = K
    left -= a

count += 1

print(count)