# Initialize variables and ask user input
num=int(input("Enter the binary number"))

i= 0 # i: Power of the base (starts from 0 )
base = 2 # base: Base of the ternary number system (2)
dec = 0 # dec: Variable to store the final decimal equivalent
is_valid = True # is_valid: Flag to check if the input number is a valid binary number
for digit in str(num):
    if digit not in "01":
        is_valid = False
        break
if not is_valid:
    print("Enter a valid binary number (digits 0, 1,  only).")
else:
        while num>0:
                rem=num%10
                dec +=rem*(base**i)
                num=num //10
                i += 1
        print(dec)