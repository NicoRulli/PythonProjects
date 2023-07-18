def runningSum(nums):
        arr = []
        count = 0
        for i in nums: 
            arr.append(0)
        for j in range(len(nums)):
            arr[j] += nums[j] + count
            count = arr[j]
        
        return arr

runningSum([1,1,1,1,1])