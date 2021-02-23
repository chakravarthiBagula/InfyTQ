import sys
"""
    Prefix sum problems.
"""
# << 1. subarray sum >>#
"""
    Q)  Given an array (A) of integers and two integers denoting the starting and ending indexes of the subarray.Your task is to find the sum of elements
    of the sub array.

        Input Format:
            first line contains  a single integer N.
            next line contains N space separated integers.
            next line contains an integer t no of testcases
            next "T" lines contains l,r separated by space.
        Output Format:
            A single integer denoting the sum of subarray.
"""

"""
    sol:
        The Basic BruteForce idea will be 
            runnig a loop through l to r
            and add all the items

            This will work Fine For the smaller testCases.
            In Case of larger testCases the time complexity
            increases.

            Time Complexity:
                O(testCases) + O(r1-l1) + O(r2 - l2) ....
                +O(r{testCase} - l{testCase}).
            
            So we have to find a way with linear complexity.

        The Idea of this approach is
            Store the cummulative sums of the array
            in another array.
            
            Example:
                arr = [1,2,3,4,5]
                cummulative_Sum = [1, 3(1+2), 6(3+3), 10(6+4), 15(10+5)]
            
            By doing this we have sums of subarrays from starting to 
            each index.

            And the sum of subarray between l and r will be
            Calulated by the formula.

                sum(l, r) = cummulative_Sum[r] - cummulative_Sum[l-1] 
            
            Time Complexity :
                O(testCases + n)
            
    Implementation:
"""


class Solution:
    def __init__(self, array=None, n=None):
        if array is None:
            array = []
        if n is None:
            n = array.__len__()
        self.array = array
        self.n = n
        self.dp = [0] * (self.n + 1)
        self.sumUp()

    def sumUp(self):
        for i in range(self.n):
            self.dp[i] = self.dp[i-1] + self.array[i]
        return

    def getSum(self, l: int, r: int):
        if (l < 0) or (r < 0) or (r < l) or (r >= self.n):
            return f"l and r should be valid positive indexes between 0...{self.n-1} and l <= r."
        return self.dp[r] - self.dp[l-1]


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    solver = Solution(array, n)
    testCases = int(input())
    for i in range(testCases):
        l, r = map(int, input().split())
        res = solver.getSum(l, r)
        print(res)
    sys.stdout.flush()
    sys.exit()
