print("=" * 50)
print("              Text Analyzer")
print("=" * 50)

text = input("Enter a sentence: ")

# Total characters
characters = len(text)

# Total words
words = len(text.split())

# Total vowels
vowels = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1

print("\n===== Analysis Result =====")
print("Total Characters :", characters)
print("Total Words      :", words)
print("Total Vowels     :", vowels)
print("Uppercase        :", text.upper())
print("Lowercase        :", text.lower())
