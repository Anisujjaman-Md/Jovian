def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) -1

    while lo <= hi:
        mid = hi //2
        mid_number = nums[mid]

        if mid > 0 and nums[mid]:
            return mid
        elif mid > 0 and nums[mid]:
            hi = mid - 1
        else:
            low = mid +1
    
    return 0