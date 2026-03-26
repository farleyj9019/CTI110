# Justin Farley
# 3/26/2026
# P1HW2_FarleyJustin.py
# A program that does some basic math on numbers that are entered


# Calculate travel expenses

print("This program calculates and displays travel expenses")
print()

num1 = int(input("Enter Budget: "))
travel_dest = input("Enter your travel destination: ")
num2 = int(input("How much do you think you will spend on gas?: "))
num3 = int(input("Approximately, how much will you need for accommodation/hotel?: "))
num4 = int(input("Last, how much do you need for food?: "))

sum_result =  num1
final_result = sum_result - num2 - num3 - num4

# Display of expense results

print("------------Travel Expenses------------")
print("Location:", travel_dest)
print("Initial Budget:", num1)
print("Fuel:", num2)
print("Accommodation:", num3)
print("Food:", num4)
print("Remaining Balance:", final_result)
