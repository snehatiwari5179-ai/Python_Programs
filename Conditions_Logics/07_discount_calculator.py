# A shop gives a 10% discount when the purchase amount is at least ₹1,000.

amount = float(input("Enter purchase amount_____"))

if amount < 0 :
     print("Invalid amount")
elif amount >= 1000 :
     discount = amount * 0.10
     final_amt = amount - discount
     print ("Discount:",discount)
     print ("Final_amount:", final_amt)
else :
     print ("No discount")
     print ("Final_amount:",amount)
     