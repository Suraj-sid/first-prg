user=input("enter the password :")
alpha=""
digit=""
special=""
for ch in user:
  if ch.isalpha():
    alpha+=ch
  elif ch.isdigit():
    digit+=ch
  else:
    special+=ch
if len(alpha)>=2 and len(digit)==1 and len(special)==1:
  print("valid")
else:
  print("invalid")
