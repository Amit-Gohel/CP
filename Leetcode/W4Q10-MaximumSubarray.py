"""

aapde minus vala starting na teram kadhi
like [-1, -2, 2, 4, -6] ne [2, 4, -6] ma convert karva nu
aane kadhava mate ak variable leva no and jiya sudhi next minus na aave tiya
sudhi nu sum leva nu and jo sum minus aave to atlo array kadhi deva no
and jo sum plus ma hoy to sum no max ak variable ma store karva no jethi 
sothi max variable jato na rahe!!

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]                            # 0 na rakhay kem ke first 
                                                    # -5 hoy to answere -5 aave
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        
        return maxSum



"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

"""