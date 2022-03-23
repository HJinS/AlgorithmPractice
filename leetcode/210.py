from collections import deque
from typing import List
# Topological sort
# 인접리스트로 구성
# 들어가는 간선의 숫자를 배열로 따로 관리
# Q 를 이용해서 들어가는 간선의 수가 0인 것들을 관리
# Q가 비었는데 node가 비었지 않으면 틀림
# 노드가 연결된 간선이 없으면 다음
# 노드 방문 후 삭제
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         
        node = {}
        inCnt = [0 for i in range(numCourses)]
        ans = []
        for a, b in prerequisites:
            if b not in node:
                node[b] = [a]
            else:
                node[b].append(a)
            inCnt[a] += 1
            
                
        def TopologicalSort():
            Q = deque()
            if inCnt.count(0) == 0:
                return False
            for i in range(numCourses):
                if inCnt[i] == 0:
                    Q.append(i)
            print(inCnt)
            for i in range(numCourses):
                if not Q and node != {}:
                    return False
                node_Num = Q.popleft()
                ans.append(node_Num)
                if not node_Num in node:
                    continue
                for adj_node in node[node_Num]:
                    inCnt[adj_node] -= 1
                    if inCnt[adj_node] == 0:
                        Q.append(adj_node)
                del node[node_Num]
        
        

        if TopologicalSort() == False:
            return []
        return ans