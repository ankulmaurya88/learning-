'''
Find the Largest Element
Traversal
O(n)


arr=[34,56,8,900,-6,100]

def largest_ele(nums:list)->int:
    largest_element=nums[0]
    size=len(nums)
    for i in range (1,size):
        if largest_element<nums[i]:
            largest_element=nums[i]
    return largest_element


Find the Largest Element
Traversal
O(n)


arr=[34,56,8,900,-6,100]

def largest_ele(nums:list)->int:
    largest_element=nums[0]
    size=len(nums)
    for i in range (1,size):
        if largest_element<nums[i]:
            largest_element=nums[i]
    return largest_element

ele=largest_ele(arr)

print(ele)

2
Find the Second Largest Element
Tracking max values
O(n)




arr=[34,56,8,8,900,900,-6,100,700]


def SecondLargestNumber(nums:list)->int:

    Frist_larget_number=float('-inf')
    Second_larget_number=float('-inf')

    size=len(nums)
    for i in range (size):
        if nums[i]>Frist_larget_number:
            Second_larget_number=Frist_larget_number
            Frist_larget_number=nums[i]

        elif nums[i]>Second_larget_number and nums[i]!=Frist_larget_number:
            Second_larget_number=nums[i]


    return Second_larget_number


find_number=SecondLargestNumber(arr)
print(find_number)





3
Check if an Array is Sorted
Traversal
O(n)



arr=[34,56,8,8,900,900,-6,100,700]


def issorted(nums:list)-> bool:

    size=len(nums)
    if size <= 1:
        return True


    for i in range (size-1):
        if nums[i] >= nums[i+1]:
            return False
        
    return True

arr = [1, 2, 3, 4]
print(issorted(arr))  # True

arr2 = [1, 3, 2]
print(issorted(arr2)) # False



4
Reverse an Array
Two Pointers
O(n)


'''
