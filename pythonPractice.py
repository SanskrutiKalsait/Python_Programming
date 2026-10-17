


# text = "Python"

# print(text[::-1])

# text = "madam"

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")

text = "education"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels =", count)

