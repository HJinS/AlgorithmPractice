class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_cnt = 0
        for num in num_set:
            # num-1이 num_set에 있으면 앞에서 카운트 했음
            if num - 1 not in num_set:
                current_num = num
                current_cnt = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_cnt += 1
                
                max_cnt = max(max_cnt, current_cnt)
        return max_cnt