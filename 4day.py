# cpu_hrs=int(input("enter number of cpu hrs:"))
# storage=int(input("enter storage in gb:"))
# data_trans=int(input("enter data transfer in gb: "))

# cpu_cost= cpu_hrs* 5
# storage_cost=storage* 2
# data_transfer=data_trans*1

# total=cpu_cost+storage_cost+data_transfer
# if cpu_hrs>100:
#     print(total+500)
# else:
#     print(total)



uptime=97.5
bill=50000
if uptime>=99.9:
    refund=0
elif uptime>=98:
    refund=bill*0.10
else:
    refund=bill*0.25
    print("refund amt",refund)