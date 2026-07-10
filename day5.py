print("="*50)
print("     Reverse String")
print("="*50)
text=input("Enter a word=")
print(text[::-1])



print("="*50)
print("     Count Vowels")
print("="*50)
word=input("Enter a word=")
count=0
for ch in word.lower():
    if ch in "aeiou":
        count +=1
print("Count=",count)


print("="*50)
print("     Palindrome")
print("="*50)
word=input("Enter your word=")
if word==word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



