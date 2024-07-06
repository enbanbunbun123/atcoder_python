def intesection_of_cuboids(A,B):
    x_min1, x_max1 = min(A[0], A[3]), max(A[0], A[3])
    y_min1, y_max1 = min(A[1], A[4]), max(A[1], A[4])
    z_min1, z_max1 = min(A[2], A[5]), max(A[2], A[5])

    x_min2, x_max2 = min(B[0], B[3]), max(B[0], B[3])
    y_min2, y_max2 = min(B[1], B[4]), max(B[1], B[4])
    z_min2, z_max2 = min(B[2], B[5]), max(B[2], B[5])

    x_overlap = max(0, min(x_max1, x_max2) - max(x_min1, x_min2))
    y_overlap = max(0, min(y_max1, y_max2) - max(y_min1, y_min2))
    z_overlap = max(0, min(z_max1, z_max2) - max(z_min1, z_min2))

    if(x_overlap > 0 and y_overlap > 0 and z_overlap > 0):
        return "Yes"
    else:
        return "No"

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = intesection_of_cuboids(A, B)
print(result)