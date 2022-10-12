from weather import *

myFile = "weather.dat"
myChoice = 0

while(True):
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set Data File Name")
    print("2. Add Weather Data")
    print("3. Print Daily Report")
    print("4. Print Historical Report")
    print("9. Exit Program\n")

    myChoice = int(input("Enter Menu Choice: "))

    if myChoice == 1:
        myFile = input("Enter Data Filename: ")
        weather = read_data(myFile)
    elif myChoice == 2:
        dt = input("Enter Date: ")
        tm = input("Enter time: ")
        t = int(input("Enter Temperature: "))
        h = int(input("Enter Humidity: "))
        r = float(input("Enter the Rainfall: "))
        weather[dt+tm] = {'t':t, 'h':h,'r':r}       #at the key [dt + tm] write the following values
        write_data(weather, myFile)
    elif myChoice == 3:
        d = input("Enter Date (YYYYMMDD): ")
        display = report_daily(weather, d)
        print(display)
    elif myChoice == 4:
        display = report_historical(weather)
        print(display)
    elif myChoice == 5:
        break
    elif myChoice == 9:
        break
