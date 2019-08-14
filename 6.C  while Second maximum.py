Statement
Given a sequence of distinct non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.

Example input
1
7
9
0

Example output
7


max = 1
sec_max = 1
a = 1
while a != 0:
  a = int(input())
  if (sec_max < a < max):
    sec_max = a
  elif (a > max):
    sec_max = max
    max = a
print(sec_max)
