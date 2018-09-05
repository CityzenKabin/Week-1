# Q. Write a Python program to replace last value of tuples in a list.

x = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in x])

# Q. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

a = "This is King kabin."
print(a.swapcase())
    
# Q. The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

Input: 
ABCDCDC
CDC

Output:
2

#Solution

input = 'ABCDCDC'
sub ='CDC'
count = 0
a = len(input)
for i in range(0,len(input)):
   if input[i:i+len(sub)]==sub:
       count += 1

print(count)
#end

# Q.Write a class in which its one method accepts a string from console and another method to print the characters that have even indexes.

class Indexes:
   def __init__(self):
       self.string=""
   def get(self):
       i = input("Enter the characters:")
       for index in range(len(i)):
           #checks the even indexes and print it
           if(index % 2 == 0):
               print(i[index], end="") 
obj = Indexes()
obj.get()


#Q. Write a class in which its one method accepts a string from console and another method to print the characters that have even indexes

#Solution

import re

string = "H1e2l3l4o5w6o7r8l9d"
string = re.sub('[^a-zA-Z]', '', string)
print (string)

#end
