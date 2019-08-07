num = int(input())
if(num%3==0 and num%5==0 and num%7==0):
  print("JugsMugsPugs")
elif(num%3==0 and num%5==0):
  print("JugsMugs")
elif(num%3==0 and num%7==0):
  print("JugsPugs")
elif(num%5==0 and num%7==0):
  print("MugsPugs")
elif(num%3==0):
  print("Jugs")
elif(num%5==0):
  print("Mugs")
elif(num%7==0):
  print("Pugs")
else:
  print(num)
