nums = [2,7,11,15]
t = 9
sum(nums, t)

dic = {}

def sum(array, target):
    for index, val  in enumerate(array): 
        diff = target - val
        if diff in dic: 
            return (dic[diff], index)
        dic[val] = index
    return 