num = int(input("Enter the ternary number :"))

# Initialize variables
# i: Power of the base (starts from 0 )
# base: Base of the ternary number system (3)
# dec: Variable to store the final decimal equivalent
# is_valid: Flag to check if the input number is a valid ternary number
i = 0
base = 3
dec = 0
is_valid = True

# Check if the input number contains only valid ternary digits (0, 1, or 2)
for digit in str(num):
    if digit not in "012":
        is_valid = False
        break

# If the number is not valid, display an error message
if not is_valid:
    print("Enter a valid ternary number (digits 0, 1, or 2 only).")
else:
    # Convert the valid ternary number to its decimal equivalent
    while num > 0:
        rem = num % 10  # Extract the last digit
        dec += rem * (base ** i)
        num = num // 10  # Remove the last digit from the number
        i += 1  # Increment the power for the next digit

    # Print the decimal equivalent
    print(dec)
