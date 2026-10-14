# rama_height=1.7
# raja_height=2.0
# if rama_height>raja_height:
#     print('rama is taller')
# else:
#     print('raja is taller')
total=float(input("entr total purchase amount"))
if total>=1000:
    discount=total*0.10
    final_amount=total-discount
    print('discount applied:',discount)
    print('')
