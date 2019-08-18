Statement
Given a list of non-zero integers, find and print the first adjacent pair of elements that have the same sign. If there is no such pair, print 0.

Example input #1
-1 2 3 -1 -2

Example output #1
2 3

Example input #2
1 -3 4 -2 1

Example output #2
0

# Read a list of integers:
a = [int(s) for s in input().split()]
# Print a value:
i = 1

for i in range(1, len(a)):
  if a[i] * a[i-1] > 0:
    print(str(a[i - 1]), str(a[i]))
    break
  elif i == len(a)-1:
    print("0")
