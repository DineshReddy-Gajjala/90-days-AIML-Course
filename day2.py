#a=int(input("Enter a number="))
#b=int(input("Enter another number="))
#print(a+b)
#print(a-b) 
#print(a*b)
#print(a/b)
#print(a%b)
#print(a**b)
#print(a//b)

name=input("Enter your name=")
Roll_no=int(input("Enter your roll number="))
telugu=int(input("Enter your telugu marks="))
english=int(input("Enter your english marks="))
maths=int(input("Enter your maths marks="))
science=int(input("Enter your science marks="))
total=telugu+english+maths+science
avg=total/4
if(avg>=90):
    print("Grade=A")
elif(avg>=80 and avg<90):
    print("Grade=B")
elif(avg>=70 and avg<80):
    print("Grade=C")
elif(avg>=60 and avg<70):
    print("Grade=D")
elif(avg>=50 and avg<60):
    print("Grade=E")
elif(avg>40 and avg<50):
    print("Grade=F")
else:
    print("Grade=Fail")
print("Name=",name)
print("Roll Number=",Roll_no)
print("Total Marks=",total)
print("Average Marks=",avg)
