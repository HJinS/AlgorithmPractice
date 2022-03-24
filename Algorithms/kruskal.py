# 정점, 간선 개수
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
    
# find
# find 하면서 깊이를 줄이기 위해 parent수정
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, x)
    return parent[x]

def union(parent, a, b):
    a_par = find(parent, a)
    b_par = find(parent, b)
    # a와 b의 부모를 찾아
    # 더 큰 쪽에 합침
    if a_par < b_par:
        parent[b_par] = a_par
    else:
        parent[a_par] = b_par


edges = []
total_cost = 0

# 그래프 구축
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
# 간선을 cost기준으로 정렬(오름차순)
edges.sort()
mst = []

# 정렬한 edge를 순차적으로 접근
# union-find를 이용하여 사이클 판별
for i in range(e):
    cost, a, b = edges[i]
    
    # find시 부모가 다르면 사이클 없음
    # union연산 실행
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        mst.append(edges[i])