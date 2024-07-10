Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

# １つのタイル内で最初の地点が右側のboxである場合、左側のboxを最初の地点にする
if (Sx + Sy) % 2 == 1:
    Sx -= 1

if (Tx + Ty) % 2 == 1:
    Tx -= 1

distanceX = abs(Tx - Sx)
distanceY = abs(Ty - Sy)

Sx = Sy = 0

# 2つのboxで1つのタイルなので、x方向の移動に関しては、2で割った値を足す
ans = distanceY + max(distanceX - distanceY, 0) // 2
print(ans)

