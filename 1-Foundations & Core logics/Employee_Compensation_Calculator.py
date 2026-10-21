
# Calculate annual salary, deductions, bonus and average monthly take-home pay.

employee = "Sneha"
monthly_salary = 42000
deduction_rate = 8
annual_bonus =  25000

annual_salary = monthly_salary * 12
deductions = annual_salary * deduction_rate / 100
take_home = annual_salary - deductions + annual_bonus
monthly_average = take_home / 12

print(f"employee: {employee}")
print(f"annual salary: Rs. {annual_salary:,.2f}")
print(f"annual_deductions: Rs.{deductions:,.2f}")
print(f"annual bonus: Rs.{annual_bonus:,.2f}")
print(f"annual take-home: Rs.{take_home:,.2f}")
print(f"monthly average: Rs.{monthly_average:,.2f}")

