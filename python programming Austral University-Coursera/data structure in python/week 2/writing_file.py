
#writing and reading fileswith keywor help to deal with file object

# preprocesors
import math
 
factorial_10 = str(math.factorial(10))
# use of \\ Unicode error, because the \u is a Unicode escape. If the next 8 characters after the \u are not numeric this produces an error.
with open ('C:\\Users\\feliu\\Documents\\Felix\\ContinueEducation\\coursera\python programming Austral University-Coursera\\data structure in python\\factorial.txt', 'w') as test_file:
    test_file.write(factorial_10)