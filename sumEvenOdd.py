"""
n = int(input("Enter The NUmber : "))
odd = []
even = []
total = []
for i in range(n):
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
total += odd + even
print("Even Number : ", even)
print("Odd Number :", odd)
print("Total is : ",(total))

"""
"""
# Input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Initialize sums
even_sum = 0
odd_sum = 0

# Loop through the range and add to respective sums
for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Output the results
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
 
"""

# Input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Initialize sums
even_sum = 0
odd_sum = 0

# Loop through the range and add to respective sums
for num in range(start, end + 1): # end + 1 ensures that the loop includes the end value in the iteration
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Add the two sums
total_sum = even_sum + odd_sum

# Output the results
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("Total sum of even and odd numbers:", total_sum)

