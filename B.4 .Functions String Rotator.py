String Rotator

Write a Python function string_rotate to generate the desired pattern. The function should accept an integer as its single argument. 

Input and Output Format:
Input consists of a single integer that corresponds to n.
Assume that 0 < n <= 26. 
Refer sample output for output formatting specifications.

Sample Input1 : 5
Sample Output1:
ABCDE
BCDEA
CDEAB
DEABC
EABCD


Sample Input2 : 6
Sample Output2:
ABCDEF
BCDEFA
CDEFAB
DEFABC
EFABCD
FABCDE

from string import ascii_uppercase
def string_rotate(num):
  str1 = ascii_uppercase[:num]
  rot = str1
  for _ in range(num-1):
    rstr1 = str1[1:] + str1[0]
    rot += " " + rstr1
    str1 = rstr1
  return rot
