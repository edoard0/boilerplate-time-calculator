def add_time(start,duration,weekday=""):
    
    weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]
    
    day_minutes=24*60
    half_day_minutes=day_minutes/2

    time_of_day=str(start.split(" ")[-1])

    start_hours=int(start.split(":")[0])

    if time_of_day=="AM":
        start_minutes=int(start.split(":")[-1].split(" ")[0])+start_hours*60
    else:
        start_minutes=int(start.split(":")[-1].split(" ")[0])+start_hours*60+int(half_day_minutes)

    duration_hours=int(duration.split(":")[0])
    duration_minutes=int(duration.split(":")[-1])+duration_hours*60

    new_time_location=start_minutes+duration_minutes

    if int(new_time_location/day_minutes)<1:
        day=""
    elif int(new_time_location/day_minutes)>=1 and int(new_time_location/day_minutes)<2:
        day="(next day)"

    else:
        day="({} days later)".format(int(new_time_location/day_minutes))


    new_time_location_minutes_passed=new_time_location%day_minutes
    new_time_location_hours=(new_time_location%day_minutes)//60
    new_time_location_minutes=(new_time_location%day_minutes)%60

    if new_time_location_minutes_passed < half_day_minutes:
        new_time_of_day="AM"
    else:
        new_time_of_day="PM"
    
    if new_time_of_day=="PM":
        new_time_location_hours=new_time_location_hours%12
        if new_time_location_hours==0:
            new_time_location_hours+=12
            
    if new_time_of_day=="AM":
        if new_time_location_hours==0:
            new_time_location_hours+=12
    
    if len(str(new_time_location_minutes))<2:
        new_time_location_minutes="0"+str(new_time_location_minutes)
    
    if not weekday:
        if not day:
            return "{}:{} {}".format(new_time_location_hours,new_time_location_minutes,new_time_of_day)
        else:
            return "{}:{} {} {}".format(new_time_location_hours,new_time_location_minutes,new_time_of_day,day)
    else:
        if day=="":
            return "{}:{} {}, {}".format(new_time_location_hours,new_time_location_minutes,new_time_of_day,weekday)
        
        elif day=="(next day)":
            new_weekday=weekdays[weekdays.index(weekday.lower().capitalize())+1]
            
            return "{}:{} {}, {} {}".format(new_time_location_hours,new_time_location_minutes,new_time_of_day,new_weekday,day)
        
        
        else:
            start_index=weekdays.index(weekday.lower().capitalize())
            days_to_add=int(day.split(" ")[0].split("(")[1])%7
            new_weekday=weekdays[start_index+days_to_add]
            return "{}:{} {}, {} {}".format(new_time_location_hours,new_time_location_minutes,new_time_of_day,new_weekday,day)

            
            

