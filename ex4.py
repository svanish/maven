cars = 100 #Total number of cars
space_in_a_car = 4 #Total number of seat in a car
drivers = 30 #Drivers available
passengers = 90 #number of passengers
cars_not_driven = cars - drivers #This will give number of cars not driven
cars_driven = drivers #Number of cars running
carpool_capacity = cars_driven * space_in_a_car #Capacity of running cars
average_passengers_per_car = passengers / cars_driven #average number of passenger in running cars


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "there will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have",passengers, "to carpool today."
print "We need to put about", average_passengers_per_car,"in each car"