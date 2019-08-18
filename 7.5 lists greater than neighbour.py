Statement
Given a list of numbers, determine and print the number of elements that are greater than both of their neighbors.

The first and the last items of the list shouldn't be considered because they don't have two neighbors.

Example input
1 5 1 5 1

Example output
2

# Read a list of integers:
a = [int(s) for s in input().split()]
gre = 0
# Print a value:
for i in range(1,len(a)-1):
  if a[i-1] < a[i] and a[i] > a[i+1]:
    gre = gre +1
print(gre)
