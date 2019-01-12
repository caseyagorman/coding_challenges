

# Given a sorted array nums, remove the duplicates in-place such that each 
# element appear only once and return the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the input array 
# in-place with O(1) extra memory.

def remove_duplicates(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i]


# Notes: delete modifies the list in place. 
# So that your deletions do not change the part of the list you have not yet 
# examined.