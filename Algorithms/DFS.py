# DFS(Depth First Search)
# 한 노드에서 다음 분기로 넘어가기 전에 해당 분기의 가장 안쪽까지 들어가고 넘어가는 탐색 방법
# 보통 재귀 형태를 뛰고있다.

# 여기서 그래프는 인접 리스트로 한다.
graph = [i  for i in range(10)] 
visited = [False for i in range(10)]
def dfs(node):
    if node == None:
        return
    visited[node] = True
    # 노드 방문
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node)
    return
    
    