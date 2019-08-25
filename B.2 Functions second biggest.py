Second Largest
Write a function second_is_second_largest that will return True if the 2nd largest value is in the 2nd position. Otherwise, return False.

The function should accept three arguments. 

Example 
second_is_second_largest(1, 2, 3) -> True 
second_is_second_largest(11, 10, 9) -> True
second_is_second_largest(3, 3, 0) -> False 
second_is_second_largest(3, 2, 2) -> False 


def second_is_second_largest(ele1,ele2,ele3):
    sec_max = ele2
    
    if((sec_max > ele3 and sec_max < ele1) or (sec_max < ele3 and sec_max > ele1 )):
        return True
    else:
        return False
