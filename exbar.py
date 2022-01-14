#EXAMPLE OUTPUT BARGRAPH

#SAVING 

#TODO: Need to do stuff lpease gelp me I need to get into the mental hiostpital
# FIXME: FIXME:



import matplotlib.pyplot as plt
import bargraphtest

Day_of_the_Week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',]
Mood_Rating = [0,0,0,0,0,0,0]
color_assoc = ['green','green','green','green','green','green','green']
Colors = ('green', 'red', 'orange', 'yellow')

# for every value in Mood_rating: figure out what color corresponds
# for loop to iterate through mood_rating 
# if mood rating = 1 then color red
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

x = bargraphtest.day_rating(Mood_Rating)

if x == 1:
	show_graph() 
	


def show_graph () -> None:
	get_colors(Mood_Rating)
	plt.bar(Day_of_the_Week, Mood_Rating, color=color_assoc)
	plt.title("Your Mood Chart for the Week", fontsize=16)
	plt.xlabel("Day of the Week", fontsize=14)
	plt.ylabel("Mood Rating", fontsize=14)
	plt.show()


# if "1" in Mood_Rating:
#   Colors = ('red')