Statement
Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.

Example input
2
apple orange banana
banana orange

Example output
banana

n = int(input())
# Print a value:n = int(input())
words ={}
myList = []
for i in range(n):
    a = list(input().split())
    for j in range(len(a)):  
        if a[j] not in words:
            words[a[j]] = 0
        words[a[j]] += 1
for k,v in words.items():
    if v >= max(words.values()):
        myList.append(k)
print(sorted(myList)[0])
