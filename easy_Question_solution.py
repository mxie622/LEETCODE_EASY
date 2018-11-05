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
#method 1: Fibonacci formula. a**2 - a - 1 = 0
class Solution:
    def climbStairs(self, n):
        output = 1 / (5 ** 0.5) * (((1 + (5 ** 0.5)) / 2) ** (n + 1) - ((1 - (5 ** 0.5)) / 2) ** (n + 1))
        return int(output)
#method2: Fibonacci series
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


#https://leetcode.com/problems/maximum-subarray/description/
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# https://leetcode.com/submissions/detail/186503256/
class Solution:
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483648 - 1
        elif 0 <= dividend * divisor:
            return dividend // divisor
        else:
            return (abs(dividend) // abs(divisor))*(-1)

# https://leetcode.com/problems/invert-binary-tree/description/
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        tmp=root.right
        root.right=self.invertTree(root.left)
        root.left=self.invertTree(tmp)
        return root

# https://leetcode.com/problems/balanced-binary-tree/description/
class Solution(object):

    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if left == -1 or right == -1 : return -1
        if abs(left - right) > 1:  return -1
        return max(left, right) + 1

    def isBalanced(self, root):
        height = self.get_height(root)
        return height != -1
