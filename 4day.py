cpu_hrs=int(input("enter number of cpu hrs:"))
storage=int(input("enter storage in gb:"))
data_trans=int(input("enter data transfer in gb: "))

cpu_cost= cpu_hrs* 5
storage_cost=storage* 2
data_transfer=data_trans*1

total=cpu_cost+storage_cost+data_transfer
if cpu_hrs>100:
    print(total+500)
else:
    print(total)