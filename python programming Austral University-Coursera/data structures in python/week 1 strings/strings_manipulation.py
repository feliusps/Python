import string
import datetime

#+++++++++++++++++++++++++++++++++
#string manipulation
#+++++++++++++++++++++++++++++++++
#what is printing?
#print("Hola \n Mundo!")

# what values return True
#a_string = 'Python'
#print(a_string.startswith('Py'))

#a_string = 'py'.capitalize()
#print(a_string.startswith('Py'))

#what values return True
#a_string = 'PYTHON'  
#print(a_string.endswith('on'.swapcase()))

#what values return True
#a_string = '\\n' 
#print(a_string.isspace())

#what values return True
#a_string = 'PyThon' 
#print(a_string.istitle())

#what values return abracadabra
#a_string = 'abracadabra' 
#print(a_string.replace('a', 'e'))

#what values return a_string
#a_string = '1, 2, 3, 4' 
#print(a_string.split(', '))

#what values return a_string
#a_string = 'PYTHON'
#print(a_string.isupper())

#how to get the string  ‘1-2-3’?
#a_list = ['1', '2', '3']
#print('-'.join(a_list) )

#==================================
#string library
#==================================
#what values return a_string
#print('{:d}'.format(2.5))

#*************************************
#date and time
#*************************************
#date = datetime.datetime(2019, 1, 1, 12, 10, 35)
#print(date)

#date = datetime.datetime(2019, 1, 1)
#print(date.year)

#date = datetime.date(2019, 2, 29)
#print(date)

#date = datetime.date.today() - datetime.timedelta(seconds=86900)
#print(date)
#date = datetime.date(2019, 12, 31)
#print(date.year)
#print(date.isoformat())

#date_time = datetime.datetime(2019, 2, 27, 11, 15, 30)
#print(date_time.strftime('%d/%m/%y %H:%M'))  #day months years hours and minutes

#date_time = '2019-01-30 15:30:45'

date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)

print(date_time.strftime('%y/%m/%d %H:%M:%S'))