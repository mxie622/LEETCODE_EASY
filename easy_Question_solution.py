#https://leetcode.com/problems/rotate-array/description/
nums = [1,2,3,4,5,6,7]
k = 3
class Solution:
    def rotate(self, nums, k):
        n = k
        inp = nums
        i = 1
        while k > 0:
            nums.insert(0, inp[len(nums) - i])
            i += 1
            k -= 1
        return nums[:-3]
print(Solution().rotate(nums, k))

#https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums):
        L = set(nums)
        C = list(L)
        n = len(nums)
        for i in C:
            if nums.count(i) > int(n/2):
                element = i
        return element

#https://leetcode.com/problems/climbing-stairs/description/
method 1:
class Solution:
    def climbStairs(self, n):
        output = 1 / (5 ** 0.5) * (((1 + (5 ** 0.5)) / 2) ** (n + 1) - ((1 - (5 ** 0.5)) / 2) ** (n + 1))
        return int(output)
method2:
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        else:
            one = 1
            two = 2
            for i in range(2, n):
                three = one + two
                one = two
                two = three
        return two

#https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        for i in range(len(nums)):
            if i ==1:
                nums[i] = max(nums[0],nums[1])
            if i >1:
                nums[i] = max(nums[i]+nums[i-2],nums[i-1])
        return max(nums)

#https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i, j):
        return sum(self.nums[i : j+1])
