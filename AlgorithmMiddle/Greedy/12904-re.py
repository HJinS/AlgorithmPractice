S = list(input())
T = list(input())

while len(S) < len(T):
    c = T[len(T)-1]
    T.pop(len(T)-1)
    if c == 'B':
        T.reverse()
if S == T:
    print(1)
else:
    print(0)