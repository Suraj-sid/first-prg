# sum and  product manual function 
# num=[10,20,30]
# total=0
# pro=1
# for x in num:
#     total=total+x
# print("sum",total)

# for y in num:
#     pro=pro*y
# print("mult",pro)

# COUNT MANUAL FUNCTION 
count=3
for x in [10,20,30]:
    count=count+1
print(count)

# SORT MANUL FUNCTION
nums=[2,5,9,1,9]
n=len(nums)
for i in range(n):
    for j in range(n-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)