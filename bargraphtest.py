#bar graph

import matplotlib.pyplot as plt

day = ['Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday',]
mood = [0,0,0,0,0,0,0 ]

def day_rating(Mood_Rating):
    try:
        import datetime
        __day = datetime.datetime.today().weekday()
        print(__day)
        feeling = input("Jae: How are you feeling?")
        Mood_Rating[__day + 1] += int(feeling)
        return 1
    except ValueError:
        print("Needs to be a number")
        return -1;
print(mood)
# day_rating()
print(mood)

