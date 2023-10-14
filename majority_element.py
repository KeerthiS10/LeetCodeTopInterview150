# Method 1
def majorityElement(nums):
    ch = {}
    for i in nums:
        if i in ch:
            ch[i] += 1
        else:
            ch[i] = 1

    num = max(ch.keys())
    return num


num = majorityElement([2, 2, 1, 1, 1, 2, 2])
print(f"Majority element is {num}.")


# Method 2
def majorityElements(num):
    num.sort()
    return num[(len(num) // 2)]
