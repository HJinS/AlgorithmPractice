Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())

def dis(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

l_x, l_y, l_z = Ax, Ay, Az
r_x, r_y, r_z = Bx, By, Bz
res = 987654321

dis_AC = dis(Ax, Ay, Az, Cx, Cy, Cz)
dis_BC = dis(Bx, By, Bz, Cx, Cy, Cz)

while True:
    mid_x, mid_y, mid_z = (l_x + r_x) /2, (l_y + r_y) / 2, (l_z + r_z) / 2
    dis_lC = dis(l_x, l_y, l_z, Cx, Cy, Cz)
    dis_rC = dis(r_x, r_y, r_z, Cx, Cy, Cz)
    dis_mc = dis(mid_x, mid_y, mid_z, Cx, Cy, Cz)
    
    if abs(dis_mc - res) <= 10e-7:
        break

    if dis_mc < res:
        res = dis_mc
    
    if dis_lC > dis_rC:
        l_x = mid_x
        l_y = mid_y
        l_z = mid_z
    else:
        r_x = mid_x
        r_y = mid_y
        r_z = mid_z

print(res)