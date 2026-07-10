print("="*50)
print("     Password Strength")
print("="*50)
password=input("Enter password=")
if len(password)<8:
    print("Weak")
elif len(password)>=8 and len(password)<=11:
    print("Medium")
else:
    print("Strong")
