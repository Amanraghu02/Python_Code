num = int(input("Enter a number: "))

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num - 1):   # If num is divisible by any number between 2 and num-1
       if (num % i) == 0:   #just example i gave Input: 7 The for loop checks divisors from 2 to 6
           print(num,"is not a prime number")
           #print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
#else:
   #print(num,"is not a prime number")