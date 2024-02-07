# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non - decreasing order,
# find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example
# 1:
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Example
# 2:
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
# Example
# 3:
#
# Input: nums = [], target = 0
# Output: [-1, -1]


def seachRange(input,target):
    first = findFirst(input,target)
    last = findLast(input,target)
    return [first,last]
def findFirst(input,target):
    n= len(input)
    for i in range(n):
        if input[i] == target:
            return i
    return -1
def findLast(input,target):
    n= len(input)
    for i in range(n-1,-1,-1):
        if input[i] == target:
            return i
    return -1
if __name__ == "__main__":
    inp= list(map(int,input("Please Enter Array : ").split()))
    target=int(input("Please Enter Target :  "))
    print(seachRange(inp,target))


