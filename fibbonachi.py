
num_terms = int(input("Enter the number : "))

# Initialize the first two terms
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci series:" , end=" ")
for i in range(num_terms):
    print(a, end=" ")  #The current number a is printed.The end=" "argument ensures that the numbers are 
    #printed on the same line
    a, b = b, a + b

#a takes the value of b (the next number in the Fibonacci sequence).
#b becomes the sum of the previous a and b, which is the next Fibonacci number in the sequence.


# with function

"""
def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=" ")
        fibonacci(n - 1, b, a + b)

# Number of terms in the Fibonacci series
#num_terms = 10

# Print the Fibonacci series
print("Fibonacci series:")
fibonacci(num_terms)

"""