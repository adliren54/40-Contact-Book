print("🌟Contact Card🌟\n")

name = input("Input your name > ")
dateOfBirth = input("Input your date of birth > ")
phone = input("Input your telephone number > ")
email = input("Input your email address > ")
address = input("Input your address > ")

contact = {"name":name, "date":dateOfBirth, "phone":phone, "email":email, "address":address}

print(f"Hi {contact['name']}. Our dictionary says that you were born on {contact['date']}, we can call you on {contact['phone']}, email {contact['email']}, or write to {contact['address']}.")