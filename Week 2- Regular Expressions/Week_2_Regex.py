#Questions

#Finding Numbers in a Haystack

'''In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the 
sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1637486.txt (There are 67 values and the sum ends with 540)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
Data Format
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. 
Here is a sample of the output you might see:

Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...
The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line 
(including none).
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
and then converting the extracted strings to integers and summing up the integers.

Turn in Assignent

Enter the sum from the actual data and your Python code below:
Sum:__________________ (ends with 540) '''

#Answer

#Python code:

import re

#Opening the file in which we'll need to find the numbers
sample_file = open('regex.txt')

#Obtaining strings representing the numbers in that file
text = sample_file.read() #With read, we read the entire text and not line by line
number_regex = '[0-9]+'
numbers = re.findall(number_regex, text) #Match any combination of one or more digits

#Casting them to integers and getting the total sum
total = sum(int(num) for num in numbers)

print(total)

#Closing the file to avoid memory problems
sample_file.close()