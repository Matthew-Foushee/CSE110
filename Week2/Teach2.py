firstname = input("What is your first name? ")
lastname = input("What is your last name? ").upper()
email = input("What is your email address? ").lower()
phone = input("What is your phone number? ")
jobTitle = input("What is your job title? ").title()
idNumber = input("What is your ID Number? ")

print(f"""
----------------------------------------
{lastname}, {firstname}
{jobTitle}
ID: {idNumber}

{email}
{phone}
----------------------------------------
""")