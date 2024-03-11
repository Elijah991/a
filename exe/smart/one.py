#1.Write a Python function called calculate_average that takes a list of numbers as input and returns their average.
# def calculate_average(numbers):
#     if len(numbers) == 0:
#         return 0
#     return sum(numbers) / len (numbers)

# # Example usage
# numbers_list = [5, 10, 15, 20]
# print(calculate_average(numbers_list))

#2.Define a function named is_palindrome that takes a string as an argument and returns True if it is a palindrome (reads the same forwards and backwards), and False otherwise.
# def is_palindrome(string):
#     reversed_string = string[::-1]
#     return string == reversed_string

# # Example usage
# print(is_palindrome("madam"))  # Output: True
# print(is_palindrome("python"))  # Output: False

def greet(name):
    print("Hello, " + name + "!")

# Calling the function
greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!



#3. Create a function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.
# def count_vowels(string):
#     vowel_count = 0
#     for char in string:
#         if char.lower() in 'aeiou':
#             vowel_count += 1
#     return vowel_count

# # Example usage
# print(count_vowels("Hello, World!"))  # Output: 3
# print(count_vowels("Python is awesome"))  # Output: 6


#4.Write a Python function called find_max that takes a list of numbers as input and returns the maximum value in the list.
# def find_max(numbers):
#     if len(numbers) == 0:
#         return None
#     return max(numbers)

# # Example usage
# numbers_list = [10, 5, 20, 15]
# print(find_max(numbers_list))  # Output: 20

#Define a function named is_prime that takes an integer as an argument and returns True if it is a prime number, and False otherwise.

# def is_prime (numbers):
#   if numbers <= 1:
#     return False
#   for r in range (2, int(numbers*0.5)+1):
#     if numbers % r == 0:
#       return False
#   return True
# print(is_prime(11))
# print(is_prime(3))
# print(is_prime(1))

  
  


