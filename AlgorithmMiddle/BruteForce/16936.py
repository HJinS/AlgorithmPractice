N = int(input())

B = list(map(int, input().split()))
A = list()

def check(x, B, A):
    B.remove(x)
    A.append(x)
    least_one = False
    if not B:
        return True
    if x * 2 in B:
        least_one = True
        return check(x * 2, B, A)
    if x % 3 == 0 and x // 3 in B:
        least_one = True
        return check(x // 3, B, A)
    if not least_one:
        return False
  
for i in range(N):
    A = []
    flag = check(B[i], B.copy(), A)
    if flag:
        print(*A)
        break