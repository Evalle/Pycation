# Welcome to Pycation v 0.01 

# ok, let's mortal koding begin! 
def hotel_cost(nights):
    cost = 140 * nights
    return cost
    
# check: print hotel_cost()
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
        return "I' totally don't understand you"
