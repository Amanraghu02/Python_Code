num = int(input("Enter the number : "))
if num < 0:
    print("Enter valid number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1    #After adding num to sum, num is decremented by 1. This continues until num becomes zero
    print("The sum of ",sum)

