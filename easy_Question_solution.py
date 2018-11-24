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

# https://leetcode.com/problems/implement-queue-using-stacks/description/
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.queue != []:
            a = self.queue[0]
            self.queue = self.queue[1:]
            return a

    def peek(self):

        """
        Get the front element.
        :rtype: int
        """
        if self.queue != []:
            return self.queue[0]

    def empty(self):
        if self.queue == []:
            return True
        return False

# https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_dict = {'(':-1,')':1,'[':-2,']':2,'{':-3,'}':3}
        str_list = []
        for i in s:
            val = str_dict[i]
            if val<0:
                str_list.append(val)
            else:
                if str_list== []: return False
                check = str_list.pop()
                if check != -val:
                    return False
        if str_list!= []: return False
        return True

# https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0:
            return nums

        dq = collections.deque()

        for i in range(len(nums)):
            if nums[i] == 0:
                dq.append(i)
            else:
                if len(dq) != 0 and i > dq[0]:
                    tidx = dq.popleft()
                    nums[i], nums[tidx] = nums[tidx], nums[i]
                    dq.append(i)
# https://leetcode.com/problems/ugly-number/description/
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        else:
            while num % 2 == 0:
                num = num / 2
            while num % 3 == 0:
                num = num / 3
            while num % 5 == 0:
                num = num / 5
            if num == 1 or num == 2 or num == 3 or num == 5:
                return True
            else:
                return False

# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

# https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = 0
        if target == 0:
            return 0
        else:
            for i in nums:
                if target <= i:
                    a = nums.index(i)
                    break
                else:
                    a = len(nums)
            return a

# https://leetcode.com/problems/valid-mountain-array/description/
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        h = 0
        g = 0
        i = 0

        output = True
        d = []
        f = []
        if len(A) <= 2 or A[1] <= A[0] or A[len(A)-2] <= A[len(A)-1]:
            return False
        else:
            for i in range(0, A.index(max(A))):
                if 0 < A[i+1] - A[i]:
                    h += 1
                else:
                    output = False
                    break

            if h == A.index(max(A)):
                for k in range(h, len(A)-1):
                    if 0 > A[k+1] - A[k]:
                        g += 1
                    else:
                        output = False
                        break
            return output

# https://leetcode.com/problems/excel-sheet-column-title/description/
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n>0:
            s += chr((n-1)%26 + ord('A'))
            n = (n-1)//26
        return s[::-1]

# https://leetcode.com/problems/backspace-string-compare/description/
class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)