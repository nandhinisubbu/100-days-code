
year = int(input())
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("LEAP")
       else:
           print("COMMON")
   else:
       print("LEAP")
else:
   print("COMMON") 
