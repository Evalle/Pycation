# Let's compute hotel_cost
def hotel_cost(nights):
    if nights >= 1:
        return nights*40
    else:
        "Incorrect value"

# Let's compute plane ride cost
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "I'm totally don't understand you"

# Let's compute rental_car_cost
def rental_car_cost(days):
    if days >= 3 and days < 7:
        return (days*40) - 20
    elif days >=7:
        return (days*40) - 50
    else:
        return (days*40)

# Let's bring them all together
def trip_cost(city,days):
    return plane_ride_cost(city) + rental_car_cost(days)
