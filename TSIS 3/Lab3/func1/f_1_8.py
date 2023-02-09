def spy_game(nums):
    s= ''
    for i in nums:
        if i == 0 or i== 7: s+= str(i)
    print('True') if '007' in s else print('False')

 

spy_game([1,2,4,0,0,7,5, 0,0,0]) 
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0]) 
