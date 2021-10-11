#read a file in python

#preprocessor
import csv

# open and read file
with open ('C:\\Users\\feliu\\Documents\\Felix\\ContinueEducation\\coursera\python programming Austral University-Coursera\\data structure in python\\csv_file.csv', 'a') as cvsfile:
    reader = csv.reader(['Hola|, Mundo', 'Python'], escapechar='|') #escape vertical line

#create a list
file_content = list(reader)

#output 
print(file_content)