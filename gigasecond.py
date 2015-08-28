from datetime import datetime

def add_gigasecond(birthday):
    timestamp = (birthday - datetime(1970, 1, 1)).total_seconds() #Get total number of seconds since the Unix epoch in local time
    utc_offset = 5*3600 + 30*60 #IST is 5.5 hours ahead of UTC, need to subtract to keep them in the same timezone
    giga_timestamp = timestamp + 10**9 - utc_offset #Add 1 billion seconds to the timestamp, substract UTC offset
    giga_dt = datetime.fromtimestamp(giga_timestamp) #Convert timestamp back into datetime object

    return giga_dt