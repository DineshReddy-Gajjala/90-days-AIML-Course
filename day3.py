print("="*40,"ATM SYSTEM","="*40)
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
balance=10000
number=int(input("Enter your choice="))
if(number==1):
    print("your balance is=",balance)
elif(number==2):
    deposit=int(input("Enter the amount to deposit="))
    balance+=deposit
    print("your balance is=",balance)
elif(number==3):
    withdraw=int(input("Enter the amount to withdraw="))
    if(balance>=withdraw):
        balance-=withdraw
        print("your balance is=",balance)
    else:
        print("Insufficient balance")
else:
    print("thank you for using atm system")