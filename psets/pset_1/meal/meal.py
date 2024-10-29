# define the main function
def main():
    # get time from the user
    time = input("Enter time: ")

    # pass the time into the convert function
    time = convert(time)

    # determine the meal time based on the inputted time
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")

# define the convert function
def convert(time):
    # split the time into hours and minutes variables
    hours, minutes = time.split(":")

    # convert the hours & minutes to integers
    hours = int(hours)
    minutes = int(minutes)
    
    # convert the minutes into a decimal
    minutes = minutes / 60

    # add the hours and minutes together as a float
    time = float(hours + minutes)

    # return the value of time
    return time


if __name__ == "__main__":
    main()