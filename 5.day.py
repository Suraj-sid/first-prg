# weight=float(input("enter the weight:"))
# height=float(input("enter the height:"))
# bmi=weight/(height**2)
# if bmi<18.5:
#     category='under weight'
# elif bmi<25:
#     category='normal'
# elif bmi<30:
#     category='over weight'
# else:
#     category='obese'
# print("bmi:",bmi)
# print("category:",category)

# units=int(input("enter the number  unit used:"))
# if units<100:
#     bill=units*1
# elif units<200:
#     bill=100*1+(units-100)*2
# else:
#     bill=100*1+100*2+(units-200)*5
# print("Electricity BiLL",bill)

# a=int(input("enter the first angle:"))
# b=int(input("enter the secound angle:"))
# c=int(input("enter the thirs angle:"))
# if a==b and b==c and c==a:
#     print("Equilatrial triangle")
# elif a==b or b==c or a==c:
#     print("Isoscles tiangle")
# else:
#     print("Scaleence Triangle ")


# Nested if  else

age=int(input("enter the age :"))
if age>=18:
    print("allow for match")
    if age>=18 and age<30:
        print("$2 dollar")
    elif age>=30 and age<60:
        print("$1 dollar")
    else:
        print("free ticket")
else:
    print("not allowed for match")