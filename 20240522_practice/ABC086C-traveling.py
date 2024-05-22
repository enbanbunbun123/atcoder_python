def can_travel(N, plans):

    #初期値
    prev_t, prev_x, prev_y = 0, 0, 0

    for t, x, y in plans:
        dt = t - prev_t
        dist = abs(x - prev_x) + abs(y - prev_y)

        if dist > dt or (dt - dist) % 2 != 0:
            return "No"
        
        #現在の時刻、位置を更新
        prev_t, prev_x, prev_y = t, x, y

    return "Yes"

N = int(input())
plans = [tuple(map(int, input().split())) for _ in range(N)]   

print(can_travel(N, plans))