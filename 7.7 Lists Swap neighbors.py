Statement
Given a list of numbers, swap adjacent elements in each pair (swap A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element intact.

Example input
1 2 3 4 5

Example output
2 1 4 3 5

a = [int(s) for s in input().split()]
# Print a value:
for i in range(0, len(a), 2):
    temp = a.pop(i)
    a.insert(i+1, temp)
print(a)
