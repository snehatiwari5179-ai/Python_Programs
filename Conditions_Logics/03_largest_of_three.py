a = float(input("Enter 1st No.~~~~~"))
b = float(input("Enter 2nd No.~~~~~"))
c = float(input("Enter 3rd No.~~~~~"))
d = float(input("Enter 4th No.~~~~~"))

if a >= b and a >= c and a >=d :
     print ("Largest is", a)
elif b >= a and b >= c and b >=d :
     print ("Largest is", b)
elif c >= a and c >= b and c >= d :
     print ("Largest is", c)
else :
     print ("Largest is", d)

# SHORTCUT 

e = float(input("Enter 1st No.~~~~~"))
f = float(input("Enter 2nd No.~~~~~"))
g = float(input("Enter 3rd No.~~~~~"))
h = float(input("Enter 4th No.~~~~~"))
i = float(input("Enter 5th No.~~~~~"))

largest = max(e,f,g,h,i)
print ("Largest is", largest)

