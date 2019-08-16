'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


'''

def format_duration(seconds):
    minute = 60
    hour = minute*60
    day = hour*24
    year = day*365
    arr_date=[]
    str_date=''
    
    if seconds == 0:
        return 'now'
    
    year_s = seconds//year 
    if year_s > 0: 
        seconds-=(year_s*year)
        if year_s > 1:
            arr_date.append(str(year_s) + ' years')
        else:
            arr_date.append(str(year_s) + ' year')
    day_s = seconds//day
    if day_s > 0:
        seconds-=(day_s*day)
        if day_s > 1:
            arr_date.append(str(day_s) + ' days')
        else:
            arr_date.append(str(day_s) + ' day')
    hour_s = seconds//hour
    if hour_s > 0: 
        seconds-=(hour_s*hour)
        if hour_s > 1:
            arr_date.append(str(hour_s) + ' hours')
        else:
            arr_date.append(str(hour_s) + ' hour')
    minute_s = seconds//minute
    if minute_s > 0: 
        seconds-=(minute_s*minute)
        if minute_s > 1:
            arr_date.append(str(minute_s) + ' minutes')
        else:
            arr_date.append(str(minute_s) + ' minute')
    if seconds>0:
        if seconds > 1:
            arr_date.append(str(seconds) + ' seconds')
        else:
            arr_date.append(str(seconds) + ' second')
            
    if len(arr_date) == 1:
        return str(''.join(arr_date))
    elif len(arr_date) == 2:
        return str(' and '.join(arr_date))
    else:
        str_date = str(', '.join(arr_date[0:-1])) + ' and ' + str(arr_date[-1])
        return str_date
