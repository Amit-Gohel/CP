class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complimentMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            compliment = target - num
            if num in complimentMap:
                return [complimentMap[num], i]
            else:
                complimentMap[compliment] = i


s = Solution()

a = s.twoSum([3, 2, 4], 6)
print(a)


'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]


'''
