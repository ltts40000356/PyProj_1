# Finding the next Date based on a gven Date
import datetime
dateinput = input("Enter a Date in (YYYY-MM-DD) format: ")
year, month, day = map(int,dateinput.split('-'))
dateval = datetime.date(year, month, day)
print(dateval)