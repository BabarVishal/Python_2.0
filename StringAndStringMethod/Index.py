text = "  Hello Python World  "

# 1. Change case
print(text.upper())       # "  HELLO PYTHON WORLD  "
print(text.lower())       # "  hello python world  "
print(text.title())       # "  Hello Python World  "
print(text.capitalize())  # "  hello python world  "

# 2. Remove spaces
print(text.strip())       # "Hello Python World"
print(text.lstrip())      # "Hello Python World  "
print(text.rstrip())      # "  Hello Python World"

# 3. Searching
print(text.find("Python"))   # 8 (index)
print(text.startswith("  H")) # True
print(text.endswith("ld  "))  # True

# 4. Replace and split
print(text.replace("Python", "Java"))  # "  Hello Java World  "
print(text.split())                    # ['Hello', 'Python', 'World']

# 5. Join
words = ["I", "love", "Python"]
print(" ".join(words))  # "I love Python"

# 6. Count and length
print(text.count("o"))   # 3
print(len(text))         # 22

# 7. Check type
print("123".isdigit())   # True
print("abc".isalpha())   # True
print("Hello123".isalnum()) # True
print("hello".islower()) # True
print("HELLO".isupper()) # True
