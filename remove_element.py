def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return nums


ls = removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(f"List after removing the element: {ls}.")
