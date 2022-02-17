#FIXME: OUTPUT BARGRAPH


import matplotlib.pyplot as plt
import bargraphtest

Day_of_the_Week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',]
Mood_Rating = [0,0,0,0,0,0,0]
color_assoc = ['green','green','green','green','green','green','green']
Colors = ('green', 'red', 'orange', 'yellow')


def get_colors(ratings):
    counter = 0
    print("Ratings = {}".format(ratings))
    for rate in ratings:
        print(rate)
        if rate == 1:
            color_assoc[counter] = 'red'
        elif rate == 2: 
            color_assoc[counter] = 'orange'
        elif rate == 3:
            color_assoc[counter] = 'yellow'
        elif rate > 4:
            color_assoc[counter] = 'green' 
        counter+=1


def show_graph (Mood_Rating):
	get_colors(Mood_Rating)
	plt.bar(Day_of_the_Week, Mood_Rating, color=color_assoc)
	plt.title("Your Mood Chart for the Week", fontsize=16)
	plt.xlabel("Day of the Week", fontsize=14)
	plt.ylabel("Mood Rating", fontsize=14)
	plt.show()




def data (filename):
    mood = []
    file = open(filename,"r")
    for data in file:
        data = data.strip("\n")
        mood.append(int(data))
    return mood
