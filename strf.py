Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> from datetime import datetime as n
>>> m=n.today()
>>> m
datetime.datetime(2019, 11, 29, 21, 43, 8, 337202)
>>> a=m.strftime("%Z")
>>> a
''
>>> a=m.strftime("%T")
>>> a
'21:43:08'
>>> a=m.strftime("%C")
>>> a
'20'
>>> a=m.strftime("%U")
>>> a
'47'
>>> a=m.strftime("%H %M %S")
>>> a
'21 43 08'
>>> #- %H-Two digit representation of the hour in 24-hour format
>>> # %M- Two digit representation of the minute
>>> # %S- Two digit representation of the second
>>> # %T- same as ("%H %M %S")
>>> # %U- Week number of the given year, starting with the first Sunday as the first week
>>> # %C- Two digit representation of the century (year divided by 100, truncated to an integer)
