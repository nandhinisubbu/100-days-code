JugsMugsPugsPlus and Reverse
Write a program that receives a number on the input.
It also should receive another boolean value 'rev' on the input. 

  - If the number is a multiple of 3, or it contains digit 3, it prints "Jugs". 
  - If the number is a multiple of 5, or it contains digit 5, it prints "Mugs".
  - If the number is a multiple of 7, or it contains digit 7, it prints "Pugs".

  - If the number is a multiple of both 3 and 5, it prints "JugsMugs".
        - also if number contains 3 and 5, it prints "JugsMugs"
  - If the number is a multiple of both 3 and 7, it prints "JugsPugs".
        - also if number contains 3 and 7, it prints "JugsPugs"
  - If the number is a multiple of 3, 5 and 7, it prints "JugsMugPugs".
        - also if number contains 3, 5 and 7, it prints "JugsMugsPugs"

Otherwise, it prints the number.

REVERSE REQUIREMENT:
If the boolean 'rev' is True, then reverse the order of printing. 
   - "PugsJugsMugs" for multiples of 3, 5 and 7
   - "PugsMugs" for multiple of 3 and 7
   - "MugsJugs" for multiple of 3 and 5 
   - "PugsJugs" for multiple of 5 and 7
  


INPUT 
73 
False  # contains 3 and 7

OUTPUT
JugsPugs

INPUT 
73 
True  # contains 7 and 3, print reverse order

OUTPUT
PugsJugs

INPUT 
51  # multiple of 3 and contains 5

OUTPUT
JugsMugs


INPUT 
105

OUTPUT 
JugsMugsPugs



num = input()
dig = int(num)
a = num
rev = input()
if(rev == "False" or rev == "0"):
    if (dig%3==0 or dig%5==0 or dig%7==0  or '3' in num or '5' in num or '7' in num):
        a=""
        if(dig%3==0 or '3' in num):
            a="Jugs"
        if(dig%5==0 or '5' in num):
            a=a+"Mugs"
        if(dig%7==0 or '7' in num):
            a=a+"pugs"
        print(a)
    else:   
        print(num)
else:
    if (dig%3==0 or dig%5==0 or dig%7==0  or '3' in num or '5' in num or '7' in num):
        a=""
        if(dig%3==0 or '3' in num):
            a="Pugs"
        if(dig%5==0 or '5' in num):
            a=a+"Mugs"
        if(dig%7==0 or '7' in num):
            a=a+"Jugs"
        print(a)
    else:   
        print(num)
        


