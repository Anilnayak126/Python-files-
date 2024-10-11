# *args = parameter that will pack all argumnets into  a tuple
#      useful so that a  function can accept a  varying amount of arguments.


def add(*nums):
    sum = 0
    nums = list(nums)
    nums[0]=1

    for i  in nums:
        sum += i
    return  sum


print(add(0,9,3,2))
