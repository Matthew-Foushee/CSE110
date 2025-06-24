childs_meal = float(input("What is the price of a child's meal? "))
adults_meal = float(input("What is the price of an adult's meal? "))
drink_cost = float(input("What is the price of a drink? "))
drink_count = int(input("How many drinks were purchased? "))
children_count = int(input("How many children are there? "))
adults_count = int(input("How many adults are there? "))
sales_tax_rate = int(input("What is the sales tax rate? "))

sub_total = round((children_count * childs_meal)  + (adults_count * adults_meal), 2)
sales_tax = round(sub_total * sales_tax_rate / 100, 2)
total = round(sub_total + sales_tax, 2)

print(f"Subtotal: ${sub_total}")
print(f"Sales Tax: ${sales_tax}")
print(f"Total: ${total}")

payment = float(input("What is the payment amount: "))
print(f"Change: ${round(payment - total, 2)}")