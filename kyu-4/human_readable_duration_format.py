# https://www.codewars.com/kata/52742f58faf5485cae000b9a
# Human Readable Duration Format

# First Implementation 18/10/2021
def format_duration(seconds):
    if not seconds: return "now"

    seconds, minutes=seconds%60, int((seconds-(seconds % 60))/60)
    minutes, hours=minutes%60, int((minutes-(minutes%60))/60)
    hours, days=hours%24, int((hours-(hours%24))/24)
    days, years=days%365, int((days-(days%365))/365)
    time=[seconds, minutes, hours, days, years]
    
    duration=""
    time_types={"0": "second", "1": "minute", "2":"hour", "3":"day", "4":"year"}
    for i in range(4, -1, -1):
        if time[i] == 0:
            continue
        if time[i] == 1:
            duration+=", "+str(time[i])+" "+time_types[str(i)]
        else:
            duration+=", "+str(time[i])+" "+time_types[str(i)]+"s"
            
    duration=duration[2:]
    if time.count(0) < 4:
        last_coma=0
        while True:
            if duration.find(",", last_coma) == -1:
                break
            last_coma=duration.find(",", last_coma)+1
        duration=duration[:last_coma-1]+" and"+duration[last_coma:]
    return duration
