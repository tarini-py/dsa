nums = [10,9,2,5,3,7,101,18]
n = len(nums)

lis = [1] * n

for curr_elem in range(1, n):
    for i in range(0, curr_elem):
        if nums[i] < nums[curr_elem]:
            print(curr_elem, i)
            lis[curr_elem] = max( lis[curr_elem], lis[i] + 1 )

print(lis)