num=int(input("Enter the decimal number"))
list_binary=[]
if num ==0:
    print(list_binary.append(0))
else:
    while num>0:
        rem=num%2
        list_binary.insert(0,rem)
        num=num //2
print(list_binary)
