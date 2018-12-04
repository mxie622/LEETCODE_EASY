#https://leetcode.com/problems/rotate-array/description/
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
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
# Input: [2,2,1,1,1,2,2]
# Output: 2
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
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
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
# method3: General
class Solution:
    def climbStairs(self, n):
        way_list = [1,1]
        if n < 2:
            return 1
        for i in range(2,n+1):
            ways = way_list[i-2]+way_list[i-1]
            way_list.append(ways)
        return way_list[-1]

#https://leetcode.com/problems/house-robber/description/
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        for i in range(len(nums)):
            if i ==1:
                nums[i] = max(nums[0],nums[1])
            if i > 1:
                nums[i] = max(nums[i]+nums[i-2],nums[i-1])
        return max(nums)

#https://leetcode.com/problems/range-sum-query-immutable/description/
# Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
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

# https://leetcode.com/problems/divide-two-integers/description/
# Input: dividend = 7, divisor = -3
# Output: -2
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
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
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
# Input: "([)]"
# Output: false
# Input: "{[]}"
# Output: true
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
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
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
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.

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
# Input: [1,2,3,4]
# Output: false
# Input: [1,2,3,1]
# Output: true
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

# https://leetcode.com/problems/search-insert-position/description/
# Input: [1,3,5,6], 2
# Output: 1
# Input: [1,3,5,6], 0
# Output: 0
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
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]
# Input: [0,3,2,1]
# Output: true
# Input: [3,5,5]
# Output: false

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

# https://leetcode.com/problems/number-of-recent-calls/description/
# Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
# Output: [null,1,2,3,3]
class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)

# https://leetcode.com/problems/power-of-two/description/
# Example 2:
#
# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:
#
# Input: 218
# Output: false
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False;
        while n>0:
            if n == 1:
                return True;
            if n%2!=0:
                return False;
            n = n/2;

# https://leetcode.com/problems/power-of-three/description/
# Input: 9
# Output: true
# Example 4:
#
# Input: 45
# Output: false
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 0:
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            n = n / 3
# https://leetcode.com/problems/power-of-four/description/
# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
class Solution:
    def isPowerOfFour(self, n):
        while n > 1:
          n /= 4.0
        return n == 1

# https://leetcode.com/problems/single-number/description/
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

## Method1: hash table
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

## Method2: My solution:...bad time consumed
# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         a = set()
#         b = set()
#         for i in nums:
#             if i not in a:
#                 a.add(i)
#             else:
#                 b.add(i)
#         a = list(a)
#         b = list(b)
#         print(b)
#
#         for j in a:
#             if j not in b:
#                 a = j
#         return a

## Method3: Regular expression
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         a = 0
#         for i in nums:
#             a ^= i
#             print(a)
#         return a

# https://leetcode.com/problems/missing-number/description/
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


# https://leetcode.com/problems/hamming-distance/description/
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# Method1: Use 'bin' function
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

# Method2: Bit manipulation
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            if (x & 1) ^ (y & 1) == 1:
                res += 1
            x >>= 1
            y >>= 1
        return res

# -----------Quick Sort Method------------
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))