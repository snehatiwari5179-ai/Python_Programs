
# Calculate closing inventory and the number of complete cartons required to reach a target stock level.

opening_stock = 850
received_stock = 400
units_sold = 975
target_stock = 600
carton_size = 24

closing_stock = opening_stock + received_stock - units_sold
shortage = target_stock - closing_stock

full_cartons = shortage // carton_size
remaining_units = shortage % carton_size 

cartons_to_order = full_cartons + (remaining_units > 0)

print(f"Closing_Stock: {closing_stock}")
print(f"Shortage: {shortage}")
print(f"Full cartons: {full_cartons}")
print(f"Remaining Units: {remaining_units}")
print(f"Required cartons: {cartons_to_order}")

