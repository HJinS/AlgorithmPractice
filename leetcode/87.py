from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        
        @lru_cache(None)
        def recurse(a, b):
            # 기본 조건
            if a == b: return True
            
            # 틀린 경우
            if len(a) <= 1: return False
            
            # a 와 b는 길이가 같다
            N = len(a)
            for i in range(1,N):
                # 조건1 swap된 경우 왼쪽 i개, 오른쪽 i개 확인 및 오른쪽 N-i개 왼쪽 N-i개 확인
                contd1 = recurse(a[:i], b[-i:]) and recurse(a[i:], b[:-i])
                # 조건2 swap안된 경우  왼쪽 i개(a, b) 오른쪽 N-i개(a,b)확인
                contd2 = recurse(a[:i], b[:i]) and recurse(a[i:], b[i:])
                
                # 둘 중 하나라도 맞으면 scramble 맞음
                if (contd1 or contd2):
                    return True
            # 아닐 경우 틀림
            return False        
            
        return recurse(s1, s2)  