hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura # find a total of all minutes

hour = hour + mins // 60 # find a number of hours in the minutes and add to inputted hours

mins = mins % 60 # calculate the amount of minutes left over after removing hours

hour = hour % 24 # enusre that the hours to fall within the 23 hours for millitary time format

print(hour, ":", mins, sep='')
