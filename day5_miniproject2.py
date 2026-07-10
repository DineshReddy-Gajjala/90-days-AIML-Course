print("="*50)
print("          Email Validator")
print("="*50)
email=input("Enter your email Adress=")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid")
