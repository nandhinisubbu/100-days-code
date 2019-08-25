Second Biggest Value
Write a function second_biggest_value which accepts three integers, and does the following:
returns the second biggest value among the three
returns “NA” if there are two or more equal values

Come up with a solution which does not use sorting!


Example

(1, 2, 3) -> 2
(3, 1, -1) -> 1
(3, 5, -1) -> 3
(3, -1, -1) -> "NA"

def second_biggest_value(e1,e2,e3):
  if((e1 > e2 and e1 < e3) or (e1 > e3 and e1 < e2)):
    return e1
  elif((e2 > e3 and e2 <e1) or (e2 > e1 and e2 < e3)):
    return e2
  elif((e3 > e2 and e3 < e1) or (e3 > e1 and e3 < e2)):
    return e3
  else:
    return 'NA'
