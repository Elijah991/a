num = int(input("Enter the number here:"))

while num < 1 or num > 5:
  print(f"invaid {num}")
  num = int(input("Enter the number here:"))

print(f"Your number is {num}")

