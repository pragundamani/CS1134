def shift(nums,shifts,direction="left"):
    if direction=="right":
        nums[:] = nums[-shifts:] + nums[:-shifts]
    else:
        for i in range(len(nums)-shifts):
            nums[i], nums[i+shifts] = nums[i+shifts], nums[i]
    

# nums = [1,2,3,4,5,6]
# shift(nums,2,"right")
# print(nums)