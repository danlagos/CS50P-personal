def main():
    converted_time = convert(input("what time is it? "))
    time_to_eat(converted_time)

def convert(time):
    hour, minute = time.split(":") #split hours and minutes
    hour = float(hour) # change to float
    minute = float(minute)/60 # change to float, and turn to decimal
    
    converted_time = hour + minute
    return converted_time

def time_to_eat(converted_time):
    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")
    else:
        pass
    
if __name__ == "__main__":
    main()