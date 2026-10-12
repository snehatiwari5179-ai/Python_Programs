year = int(input("Enter a Year `````"))

if year % 400 == 0 :
     print ("Leap year")
elif year % 100 == 0 :
     print ("Not a Leap year")
elif year % 4 == 0 :
     print ("Leap Year")
else :
     print ("Not a Leap Year")

# SHORTCUT

year = int(input("Enter a Year `````"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
     print ("Leap Year")
else :
     print ("Not a Leap Year")


