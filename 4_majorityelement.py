# finding the majority element using python.
# nums = [5,5,2,2,2,5,5,5]
def majorityelement(nums):
    count=0
    major_element=0
    for i in nums:
        if count==0:
            major_element=i
        if major_element==i:
            count = count + 1
        else:
            count = count - 1
    return major_element
nums = [5,5,2,2,2,5,5,5]
print(majorityelement(nums))    