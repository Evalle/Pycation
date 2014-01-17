# Let's compute hotel_cost 
def hotel_cost(nights):
    cost = 140 * nights
    return cost    
# check block
# print hotel_cost()

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
    rrc = days * 40
    if days >= 7:
        return rrc - 20
    elif days >= 3:
        return rrc - 50
    else:
        return rrc


# check block
#def new_function(nights,city):
#    summ = hotel_cost(nights) + plane_ride_cost(city)
#    return summ
#
# print new_function(2,"Tampa")
