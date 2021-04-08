Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())

def dis(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

l_x, l_y, l_z = Ax, Ay, Az
r_x, r_y, r_z = Bx, By, Bz

res = 987654321

while True:
    mid_x, mid_y, mid_z = (l_x + r_x) / 2, (l_y + r_y) / 2, (l_z + r_z) / 2
    dis_mid = dis(mid_x, mid_y, mid_z, Cx, Cy, Cz)
    dis_left = dis(l_x, l_y, l_z, Cx, Cy, Cz)
    dis_right = dis(r_x, r_y, r_z, Cx, Cy, Cz)

    if abs(res-dis_mid) < 10e-7:
        break
    if res > dis_mid:
        res = dis_mid

    if dis_left > dis_right:
        l_x = mid_x
        l_y = mid_y
        l_z = mid_z
    else:
        r_x = mid_x
        r_y = mid_y
        r_z = mid_z
print(res)