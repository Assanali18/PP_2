def has_33(nums):
    nums.append(0)
    for i in range (len(nums)-1):
        if nums[i] == 3 and nums[i+1]==3:
            print('True')
            return True
    print('False')
    return False

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 