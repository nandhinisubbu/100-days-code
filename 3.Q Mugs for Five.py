num= int(input())
if(num%3==0 and num%5==0):
  print("JugsMugs")
elif(num%3==0):
  print("Jugs")
elif(num%5==0):
  print("Mugs")
else:
  print(num)
