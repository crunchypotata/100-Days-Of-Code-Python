print("🌟Contact Card🌟")
print()

name = input("Your name > ").strip().capitalize()
data = input("Your data of bitrth > ").strip().capitalize()
phone = input("Your phone > ").strip().capitalize()
email = input("Your email > ").strip().capitalize() 
adress = input("Your adress > ").strip().capitalize()

myUser = {'name': name, 'data': data, 'phone' : phone, 'email': email, 'adress': adress}


print(f"""Hi {myUser['name']}, you was born in {myUser['data']}, we can call you on {myUser['phone']}, email {myUser['email']}, or or write to {myUser['adress']}""")
