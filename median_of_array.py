# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
import math
from statistics import median

nums1 = [1,3]
nums2 = [2,4]

full_list = nums1 + nums2 # Combines List
full_list.sort() # Sorts List O(nlogn)
print(full_list)

length = len(full_list)
length2 = length / 2

if length % 2 == 0: 
    one = math.floor(length2)
    two = math.floor(length2) + 1
    print(one, two)
    mean = (full_list[one - 1] + full_list[two - 1]) / 2
    med = mean
    print('The median of the combined list is', med)

else: 
    one = length / 2
    med = full_list[math.floor(one)]
    print('The median of the combined list is', med)


