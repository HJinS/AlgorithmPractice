from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, diff = 0, float("inf")
        n = len(nums)
        # 정렬을 해서 mid값을 start의 바로 다음으로 하고, end를 마지막 값으로 함
        for start in range(n-2):
            mid, end = start+1, n-1
            # mid와 end를 가지고 two pointer 시작
            while mid < end:
                sums = nums[start] + nums[mid] + nums[end]
                # 같으면 정답
                if sums == target:
                    return sums
                # 차이 값이 더 작으면 diff 수정, ans 수정
                if abs(sums-target) <= diff:
                    diff = abs(sums-target)
                    ans = sums
                # 합이 target보다 작으면 mid += 1
                # 합이 더 커져야함(정렬 돼 있음)
                if sums < target:
                    mid += 1
                # 합이 target보다 크거나 같으면 end -= 1
                # 합이 더 작아져야함(정렬 돼 있음)
                else:
                    end -= 1
        
        return ans