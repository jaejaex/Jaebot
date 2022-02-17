#TODO: INPUT INTERFACE

import matplotlib.pyplot as plt

day = ['Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday',]
mood = [0,0,0,0,0,0,0 ]

def day_rating(Mood_Rating):
    try:
        import datetime
        __day = datetime.datetime.today().weekday()
        # print(__day)
        feeling = input("Jae: How are you feeling today on a scale of 1-5?")
        Mood_Rating[__day + 1] += int(feeling)
        return int(feeling)
    except ValueError:
        print("Needs to be a number")
        return -1;
print(mood)
# day_rating()
print(mood)

