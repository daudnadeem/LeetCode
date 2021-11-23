# INITIAL ATTEMPT THAT IS WRONG       
def twoSum1(nums, target):
    rslts = []
    for i in range(len(nums) -1):
        if nums[i] + nums[i + 1] == target:
            rslts.append(i)
            rslts.append(i+1)
    return rslts


# APPROVED NAIVE APPROACH
def twoSum2(nums, target):
    rslts = []
    for i in range(len(nums) -1 ):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                rslts.append(i)
                rslts.append(j)
    return rslts


# O(n) approach
# Optimal answer from Leetcode
def twoSum3(nums, target):
    _dict = {}
    for i in range(len(nums)):
        result = target - nums[i]
        if result in _dict:
                return sorted([i, _dict[result]])
        _dict[nums[i]] = i

      

nums = [2,7,11,15]
target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6

# nums = [2,3,7,8,11,15]
# target = 9

print(twoSum1(nums, target))
# print(twoSum2(nums, target))
# print(twoSum3(nums, target))
