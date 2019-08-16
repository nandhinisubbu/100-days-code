Given a string in which the letter h occurs at least twice, replace every occurrence of the letter h by the letter H, except for the first and the last ones.

Example input
In the hole in the ground there lived a hobbit

Example output
In the Hole in tHe ground tHere lived a hobbit

s = input()

s1 = s[s.find("h")+1:s.rfind("h")]
s2 = s[:s.find("h")+1] + s1.replace("h","H") + s[s.rfind("h"):] 

print(s2)
