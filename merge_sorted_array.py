def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for j in range(n):
        nums1[m + j] = nums2[j]
    nums1.sort()
    return nums1


merge_list = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(f"The merged sorted list is : {merge_list}")
