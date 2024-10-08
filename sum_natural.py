num = int(input("Enter the number : "))
"""
# Initialize sum to 0
sum_of_natural_numbers = 0              # with for loop solution

for i in range(1, num + 1):
    sum_of_natural_numbers += i

print(f"The sum of the first {num} natural numbers is: {sum_of_natural_numbers}")
"""

# while loop use

# Sum of natural numbers up to num
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1  # num is decremented by 1 (i.e., num -= 1) in each iteration
   print("The sum is", sum)


