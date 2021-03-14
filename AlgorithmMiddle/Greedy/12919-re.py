S = list(input())
T = list(input())
flag = False
def solve():
    global flag
    if len(S) == len(T):
        if S == T:
            flag = True
        return
    if T[-1] == 'A':
        T.pop(-1)
        solve()
        T.append('A')
    if T[0] == 'B':
        T.pop(0)
        T.reverse()
        solve()
        T.reverse()
        T.insert(0, 'B')
solve()
if flag:
    print(1)
else:
    print(0)