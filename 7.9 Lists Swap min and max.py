Statement
Given a list of distinct numbers, swap the minimum and the maximum and print the resulting list.

Example input
3 4 5 2 1

Example output
3 4 1 2 5

a = [int(s) for s in input().split()]
# Print a value:

max = a.index(max(a))
min = a.index(min(a))
a[max], a[min] = a[min], a[max]

print(a)
