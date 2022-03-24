from collections import defaultdict, deque
from itertools import combinations
from typing import List
import math
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        total_node = len(points)
        visited = [False for i in range(total_node)]
        for i in range(len(points)):
            points[i] = points[i] + [i]
            
        total_cost = 0
        edges_used = 0
        min_dis = [math.inf] * total_node
        min_dis[0] = 0
        
        # prim알고리즘을 간선이 아닌 정점을 기준으로 적용한다.
        while edges_used < total_node:
            curr_min = math.inf
            curr_node = -1
            
            # 우선순위큐를 이용하는 대신 min_dis배열을 이용해
            # 최소 cost 간선을 찾는다
            for node in range(total_node):
                if not visited[node] and curr_min > min_dis[node]:
                    curr_min = min_dis[node]
                    curr_node = node
                    
            total_cost += curr_min
            edges_used += 1
            visited[curr_node] = True
            
            # curr_node와 next_node의 최솟값을 갱신한다.
            # min_dis에 있는 최솟값이랑 curr_node와 next_node사이의 최솟값을 비교하여 갱신한다.
            # min_dis[node]에는 node와 node의 이전 노드들사이의 거리중 최솟값이 들어간다.
            for next_node in range(total_node):
                cost = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                if not visited[next_node] and min_dis[next_node] > cost:
                    min_dis[next_node] = cost
        
        return total_cost
            
            
        