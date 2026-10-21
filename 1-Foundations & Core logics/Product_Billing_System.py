
# Calculate a Bill containing multiple products, apply a 10% discount to the subtotal, and then add 18% tax to calculate the Final Bill.

product_1 = "Keyboard"
price_1 = 1200
quantity_1 = 2

product_2 = "Mouse"
price_2 = 650
quantity_2 = 3

subtotal = price_1 * quantity_1 + price_2 * quantity_2
discount = subtotal * 10 / 100
taxable_amount = subtotal - discount
tax = taxable_amount * 18 / 100
final_total = taxable_amount + tax 

print("INVOICE")
print(f"{product_1}: Rs. {price_1 * quantity_1:,.2f}")
print(f"{product_2}: Rs. {price_2 * quantity_2:,.2f}")
print(f"SUBTOTAL: Rs.{subtotal:,.2f}")
print(f"DISCOUNT: Rs.{discount:,.2f}")
print(f"TAX: Rs.{tax:,.2f}")
print(f"FINAL_TOTAL: Rs.{final_total:,.2f}")
