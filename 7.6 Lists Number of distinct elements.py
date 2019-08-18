Statement
Given a list of numbers with all elements sorted in ascending order, determine and print the number of distinct elements in it.

Example input
1 2 2 3 3 3

Example output
3

a = [int(s) for s in input().split()]
# Print a value:
dis = 1
for i in range(1, len(a)):
  if a[i-1] != a[i]:
    dis += 1
  
print(dis)
