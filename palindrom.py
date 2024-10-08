num = int(input("Enter the number : "))
temp = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if reverse == temp:
    print("it is palindrome")
else:
    print("it is not palindrome")