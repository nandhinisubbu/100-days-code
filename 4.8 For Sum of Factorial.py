Statement
In mathematics, the factorial of an integer n, denoted by n! is the following product:

n! = 1 × 2 × … × n

For the given integer n calculate the value 

1! + 2! + 3! + ... + n!

Try to discover the solution that uses only one for-loop. And don't use math module in this exercise.

Example input
4

Example output
33



# Read an integer:
num = int(input())
# Print a value:
fact=1
sum = 0
for i in range(1,num+1):
    fact=fact*i
    i=i+1
    sum += fact
print(sum)
