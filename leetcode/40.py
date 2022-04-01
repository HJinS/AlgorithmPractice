from collections import deque
import sys
from typing import List
sys.setrecursionlimit(10000000)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        length = len(candidates)
        ans = deque()
        def comb(idx, res, SUM):
            if SUM == target:
                res = list(res)
                res.sort()
                if res not in ans:
                    ans.append(res)
                return
            if SUM > target:
                return
            for i in range(idx, length):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                res.append(candidates[i])
                SUM += candidates[i]
                comb(i+1, res, SUM)
                SUM -= candidates[i]
                res.pop()
            return
        comb(0, deque(), 0)
        return ans
                
            