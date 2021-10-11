x=int(input("enter your x"))
y=int(input("enter your y"))
x2=int(input("enter your x2"))
y2=int(input("enter your y2"))
x3=int(input("enter your x3"))
y3=int(input("enter your y3"))


slope=x*(y2-y3)+x2*(y3-y)+x3*(y-y2)

if slope==0:
   print("line check")
