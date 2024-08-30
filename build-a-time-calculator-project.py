def add_time(start, duration,day_of_week = False):
    weeks_array = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    flip_am_or_pm = {'AM':'PM','PM':'AM'}
    new_time = ''
    start_hour,start_time = int(start.split(':')[0]),start.split(':')[1]
    start_min,am_or_pm = int(start_time.split(' ')[0]),start_time.split(' ')[1]
    duration_hour,duration_min = int(duration.split(':')[0]),int(duration.split(':')[1])
 
    no_of_days = int(int(duration_hour) / 24)
    am_pm = int(start_hour + duration_hour / 12)
    after_min = start_min + duration_min
    if after_min > 60:
        start_hour  +=  1
        after_min = after_min%60
    am_pm = int((start_hour + duration_hour) / 12)
    after_hour = (start_hour + duration_hour) % 12 
    if after_min < 10:
        after_min = '0' + str(after_min)


    if after_hour == 0:
        after_hour = 12
    else:
        after_hour

    if am_or_pm == 'PM' and start_hour + (duration_hour % 12) >= 12:
        no_of_days += 1
    elif am_or_pm == 'PM' and am_pm >= 1:
        no_of_days += 1

    if am_pm > 0:
        if am_pm %2 == 1:
            am_or_pm = flip_am_or_pm[am_or_pm]

    new_time += str(after_hour) + ':' + str(after_min) + ' ' + str(am_or_pm) 


    if day_of_week:
        current_day =  weeks_array.index(day_of_week.capitalize())
        index = (current_day + no_of_days) %  7
        week_day = weeks_array[index]
        new_time += ', ' + week_day  

    if no_of_days > 1:
        new_time +=' ' + f'({no_of_days} days later)'
    elif no_of_days < 2 and am_pm > 1:
        new_time += ' ' + '(next day)'
    elif no_of_days == 1:
        new_time += ' ' + '(next day)'
        





    return new_time




