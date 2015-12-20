#! Python2

def leapYear(year):
    if year % 4 == 0:
        if (year % 100)==0 and (year % 400)==0:
            return 1
        elif (year % 100)!=0:
            return 1
        else:
            return 0
    else:
        return 0

months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
currentDate=5
currentMonth=1
currentYear=1901

count=0
while 1:
    currentDate+=7  #date increment
    mCount=months[currentMonth]
    #special leap year february month check
    if currentMonth==2 and leapYear(currentYear):
        mCount+=1
    if currentDate > mCount:  #month increment
        currentMonth+=1
        currentDate=currentDate - mCount
    if currentMonth > 12:   # year increment
        currentYear+=1
        currentMonth=1
    if currentYear == 2001:
        break
    if currentDate == 1:
        count+=1

print count
        
