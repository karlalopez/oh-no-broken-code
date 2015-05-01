# This file has a few mistakes and some things I forgot to put in.
# When I run it I don't get anything... can you fix it so I
# get asked for my vacation spot, and get a recommendation?
# Hint:
# Start at the bottom and work upwards.


vacation_spots = ['Tahoe', 'Hawaii', 'New York', 'Mexico']

seasons = ['spring', 'summer', 'fall', 'winter']

weather_patterns = {
    'spring': 'rain',
    'summer': 'sun',
    'fall': 'wind',
    'winter': 'snow'
}

activities = {
    'rain': 'visiting museums',
    'wind': 'kiteboarding',
    'sun': 'sunbathing',
    'snow': 'skiing'
}

spots_by_weather = {
    'snow' : 'Tahoe',
    'wind' : 'Hawaii',
    'rain' : 'New York',
    'sun' : 'Mexico',
}


def best_vacation_spot(weather):
    # Look at the weather type and return the vacation spot that
    # is the best for that weather.
    # You can use this mapping:
    # snow = Tahoe
    # wind = Hawaii
    # rain = New York
    # sun = Mexico
    spot = spots_by_weather[weather]
    return spot


def vacation_activity(weather_type):
    # Look up the vacation activity from activities
    # and return just the activity itself
    activity = activities[weather_type]
    return activity


def get_my_vacation():

    season_travel = raw_input("What season do you want to travel? ")

    # check if season is in the seasons list
    if season_travel not in seasons:
        print "Sorry, that isn't a season. I can't help you."
    else:
        # look up the weather type for that season
        weather = weather_patterns[season_travel]

        # get the best vacation spot for that type
        spot = best_vacation_spot(weather)

        # get the best vacation activity for that type
        activity = vacation_activity(weather)

        print "You should travel to {}, where you can spend your time {}!".format(spot, activity)


if __name__=="__main__":
    print "Welcome to the Vacation-o-Matic!"
    get_my_vacation()
