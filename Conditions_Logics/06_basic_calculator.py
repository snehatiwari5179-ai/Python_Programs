a = float(input("enter 1st num_____"))
op = input("enter operator (+,-,*,/)____")
b = float(input("enter 2nd num_____"))

if op == "+" :
     print("RESULT:",a+b)
elif op == "-" :
     print("RESULT:",a-b)
elif op == "*" :
     print("RESULT:",a*b)
elif op == "/" :
     if b == 0 :
          print("Cannot divide by 0")
     else :
          print("RESULT:",a/b) 
else :
     print("Invalid operator")    