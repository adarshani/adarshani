def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "Charlotte"==city:
        return 183
    elif "Tampa"==city:
        return 220
    elif"Pittsburgh"==city:
        return 222
    elif "Los Angels"==city:
        return 475
    
def  rental_car_cost(days):
    if days>=7:
     return 40*days - 50
    elif days>=7:
     return 40*days - 20
    if days>=7:
     return 40*days 
    
def trip_cost(city, days, spending_money):
   return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money

print("cost of car rental",rental_car_cost(6))

print("cost of plan eride",plane_ride_cost("Los Angels"))

print("cost of hotel room",hotel_cost("Los Angels"))

print("trip cost",("Tampa,6,500"))