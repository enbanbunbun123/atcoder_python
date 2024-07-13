# 2点間の２乗を計算する
def distane_squared(x1, y1, x2, y2):
    distance = (x1 - x2) ** 2  + (y1 - y2) ** 2
    return distance

xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

AB = distane_squared(xA, yA, xB, yB)
BC = distane_squared(xB, yB, xC, yC)
CA = distane_squared(xC, yC, xA, yA)

if (AB + BC == CA) or (BC + CA == AB) or (CA + AB == BC):
    print ("Yes")
else:
    print("No")