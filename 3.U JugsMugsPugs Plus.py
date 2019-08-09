JugsMugsPugs Plus
Write a program that receives a number on the input.

  - If the number is a multiple of 3, or it contains digit 3, it prints "Jugs". 
  - If the number is a multiple of 5, or it contains digit 5, it prints "Mugs".
  - If the number is a multiple of 7, or it contains digit 7, it prints "Pugs".

Otherwise, it prints the number.

SPECIAL REQUIREMENT: 
Try and limit the number of conditional statements to not more than 4. 
And use only one print statement.



INPUT 
73 
OUTPUT
JugsPugs

INPUT 
51  

OUTPUT
JugsMugs


INPUT 
105

OUTPUT 
JugsMugsPugs

num = input()
a = num
dig = int(num)
if (dig%3==0 or dig%5==0 or dig%7==0  or '3' in num or '5' in num or '7' in num):
  a=""
  if(dig%3==0 or '3' in num):
    a="Jugs"
  if(dig%5==0 or '5' in num):
    a = a + "Mugs"
  if(dig%7==0 or '7' in num):
    a = a + "Pugs"
print(a)

