import copy
import sys
S = list(input())
T = list(input())

flag = False
while True:
    if len(S) == len(T):
        if S == T:
            flag = True
        break
    c = T[len(T)-1]
    T.pop(len(T)-1)
    if c == 'B':
        T.reverse()

if flag:
    print(1)
else:
    print(0)