
#Save a csv file with the content of the variable a_list.

#preprocessor
import csv

#create a list
a_list = ['Pedro', 'Florencia', 'Matías', 'Jorge', 'María', 'Inés']

#write the csv file
with open ('C:\\Users\\feliu\\Documents\\Felix\\ContinueEducation\\coursera\python programming Austral University-Coursera\\data structure in python\\csv_file.csv', 'a') as cvsfile:
    writer = csv.writer(cvsfile)
    writer.writerow(a_list)

