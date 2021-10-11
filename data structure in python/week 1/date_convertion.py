import string
import datetime

#convert date to string

#create object and vaariable
date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)
print(date_time.strftime('%Y/%m/%d %H:%M:%S'))

#or year in diferent format 10 instead of 2010

date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)
print(date_time.strftime('%y/%m/%d %H:%M:%S'))