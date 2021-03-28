N = int(input())
score_list = []
for i in range(N):
    tmp = []
    name, kor, eng, math = map(str, input().split())
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    tmp.append(name)
    tmp.append(kor)
    tmp.append(eng)
    tmp.append(math)
    score_list.append(tmp)

res = sorted(score_list, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for e in res:
    print(e[0])