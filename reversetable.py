num = int(input("Enter the table : "))
for i in range(10, 0, -1):  #Start at 10.   End just before 0.   Decrement by 1 each time (-1)
    print(num, '*', i, '=', num*i)