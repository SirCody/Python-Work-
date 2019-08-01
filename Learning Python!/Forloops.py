#For Loops

locations = ["ireland", "alaska", "england", "scotland", "greece"]
for location in locations:
	print(location.title())
#Think of this as: "For every location in the list of locations, print the 
#locations name". "Location"(singular) is a temporary variable being used 
#with the for loop. 
for location in locations:
	print("I really want to visit: " + location.title())
	print(location.title() + " would be very beautiful this time of year.\n")

#Because this line is not indented, its not part of the for loop. 
print("Any of these locations would be a great visit!")
