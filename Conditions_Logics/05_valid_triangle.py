a = float(input("Enter 1st side_____"))
b = float(input("Enter 2nd side_____"))
c = float(input("Enter 3rd side_____"))

if (a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b):
     print("Valid Triangle")
else :
     print("Invalid")