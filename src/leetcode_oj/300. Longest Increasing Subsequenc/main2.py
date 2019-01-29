class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间复杂度(n(logn))
        """
        if len(nums) == 0:
            return 0
        temp = [nums[0]]

        for num in nums:
            # 二分法在temp中找到num的位置
            if num < temp[0]:
                temp[0] = num
            elif num > temp[-1]:
                temp.append(num)
            else:
                # 范围[min,max)
                min, max = 0, len(temp)
                while min < max:
                    mid = (max + min) // 2
                    if temp[mid] >= num:
                        max = mid
                    else:
                        min = mid + 1
                temp[max] = num
        return len(temp)
