# lst1=[10,20,30]
# lst2=[40,50,60]
# lst3=lst1+lst2
# print(lst1)
# print(lst3)

profit=[100,200,400,560]
max_pro=profit[0]
for p in profit:
    if p>max_pro:
        max_pro=p
print("maxmimum profit",max_pro)