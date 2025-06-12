def timeConversion(s):
    hour = int(s[:2])
    am_pm = s[-2:]
    
    if am_pm == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
            
    # Format the hour and append the rest of the string (minutes and seconds)
    return f"{hour:02d}{s[2:8]}"