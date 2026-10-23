
# A product costs ₹800 and sells for ₹1,000. Calculate profit per unit, total profit, markup and profit margin.

product = "Monitor"
cost_price = 800
selling_price = 1000
units_sold = 75

profit_per_unit = selling_price - cost_price
total_profit = profit_per_unit * units_sold
revenue = selling_price * units_sold
markup = profit_per_unit / cost_price * 100
margin = profit_per_unit / selling_price * 100

print(f"Product: {product}")
print(f"Revenue: Rs. {revenue:,.2f}")
print(f"Total profit: Rs. {total_profit:,.2f}")
print(f"Markup: {markup:.2f}%")
print(f"Profit margin: {margin:.2f}%")

