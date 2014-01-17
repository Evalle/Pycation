# Welcome to Pycation v 0.01 

# ok, let's mortal koding begin! 
def hotel_cost(nights):
    return nights * 40

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
        return "I don't understand you, please define your city from the list below: Charlotte, Pittsburgh, Los Angeles"

def rental_car_cost(days):
    return days * 40
    if days >= 3: 
        return costacar - 20
    elif days >= 7:
        return costcar - 50
    return costcar

def trip_cost(city,days):
    summ = hotel_cost(nights) + plane_ride_cost(city) + rental_car_cost(days)
    return summ
