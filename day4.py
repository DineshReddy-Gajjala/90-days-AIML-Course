#balance=1000
#while   True:
#    print("="*40,"ATM SYSTEM","="*40)
#    print("1. Check Balance")
#    print("2. Deposit")
#    print("3. Withdraw")
#    print("4. Exit")
#    number=int(input("Enter your choice="))
#    if(number==1):
#        print("your balance is=",balance)
#    elif(number==2):
#        deposit=int(input("Enter the amount to deposit="))
#        balance+=deposit
#        print("your balance is=",balance)
#    elif(number==3):
#        withdraw=int(input("Enter the amount to withdraw="))
#        if(balance>=withdraw):
#            balance-=withdraw
#            print("your balance is=",balance)
#        else:
#            print("Insufficient balance")
#    else:
#        print("thank you for using atm system")
#        break;

print("="*50)
print("Student Attendance Management System")
print("="*50)
num=int(input("Enter no of Students="))
present=0
absent=0
for i in range(num):
    name=input("Enter student name=")
    status=input("Enter status(presnt/absent)=")
    if status.upper()=="P":             
        present +=1
    else:
        absent +=1
print("="*50)
print("Attendance Summary")
print("="*50)
print("Present:", present)
print("Absent:", absent)