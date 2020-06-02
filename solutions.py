
#Runtime: O(N) where N = size of nums
#Space: O(N) where N = size of nums
def sumToN(nums, target):
    seen = {} #key stores value we've already seen, value stores index of key in nums
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return (seen[target - nums[i]], i)
        seen[nums[i]] = i

#Runtime: O(N) where N = number of digits in N
#Memory: O(N) where N = number of digits in N
def palindrome(num):
    num_str = str(num)
    left = 0
    right = len(num_str) - 1
    while left <= right:
        if num_str[left] != num_str[right]:
            return False
        left += 1
        right -= 1
    return True