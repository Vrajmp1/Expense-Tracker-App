#date checker

#returns True if date is in between parameters, False otherwise

month_to_digit = {'Jan':1,
                  'Feb':2,
                  'Mar':3,
                  'Apr':4,
                  'May':5,
                  'Jun':6,
                  'Jul':7,
                  'Aug':8,
                  'Sep':9,
                  'Oct':10,
                  'Nov':11,
                  'Dec':12}

days_in_months = {1:31,
                  2:28,
                  3:31,
                  4:30,
                  5:31,
                  6:30,
                  7:31,
                  8:31,
                  9:30,
                  10:31,
                  11:30,
                  12:31}

def check_between(month1,day1,year1,month2,day2,year2,m,d,y):
    if year1<y and y<year2:
        return True
    elif y<year1 or y>year2:
        return False
    elif month1<m and m<month2:
        return True
    elif m<month1 or m>month2:
        return False
    elif day1<d and d<day2:
        return True
    elif d<day1 or d>day2:
        return False
    else:
        return True

'''
month1,day1,year1 = 1,1,2022
month2,day2,year2 = 5,17,2022
m,d,y = 7,18,2022

print(check_between(month1,day1,year1,month2,day2,year2,m,d,y))

#import Age_and_Time_Calculator as agt
from datetime import date

today = str(date.today()).split('-')
'''
