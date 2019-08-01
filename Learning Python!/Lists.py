#Lists and elements in a list:
#Creating a list (line 10)
#Modifying lists and elements (line 27)
#Adding an element in a list (line 46)
#Removing an element in a list (line 63)
#Sorting lists (line 71)
#Reversing lists (line 90)
#Find length of list (line 98)

#create a list:
Dogs = ["Beagle", "Golden Retreiver", "Husky", "Black Lab"]

print(Dogs) 
print(Dogs[0])#Lets print the first element without the brackets
#Using some string methods to adjust case. 
print(Dogs[0].upper())
print(Dogs[1].lower())
print(Dogs[1].title())
#Accessing the last element in a list and going backwards:
print(Dogs[-1])
print(Dogs[-2])
#Compose a message using a list:
message = "I have a " + Dogs[1] + " and " + Dogs[-1] + " mix. I also have a " + Dogs[-2] + " mix as well."
print(message)


#Modifying Lists and elements:
motorcycles = ["honda", "yamaha", "harley"]
print(motorcycles[0])
#Change the element and print it
motorcycles[0] = "ducati"
print(motorcycles[0])
#Permanent change? yes.
#Adding elements using the append() method:
motorcycles.append("ducati")
print(motorcycles)
#creating an empty list, adding elements using append() method:
Dogs = []
Dogs.append("Lab")
Dogs.append("Husky")
Dogs.append("Beagle")
print(Dogs)
print(Dogs[1])


#Adding an element anywhere in the list:
Dogs.insert(1, "Weiner")
print(Dogs)
#Remove elemets from a list using del:
#del makes it so that the element is completely removed, unable to be used
#unless addded again.
del Dogs[1]
print(Dogs)
#however, the pop() method "pops" it off the list so that the position 
#can be used again. 
#Pops off the last item in the list
Dogs.pop()
print(Dogs)
#Pops off a specific item in the list and assigns to variable to be used:
Dogs_pop = Dogs.pop(0)
print(Dogs_pop)

#Remove an element based on position
Dogs = ["Beagle", "Golden Retreiver", "Husky", "Black Lab"]
never_owned = Dogs[0]
Dogs.remove(never_owned)
print(Dogs)
print("\nI never owned a " + never_owned + ", thats why its not on the list")


#Organizing lists:
#Using sort() method to alphabetize. 
dogs = ["Beagle", "Golden Retreiver", "Husky", "Black Lab"]
dogs.sort()
print(dogs)
#reverse alphabeticly:
dogs.sort(reverse = True) #This is a permanent sort. 
print(dogs)

#Sorting temporarily using sorted() function. This does not affect the list, just
#the display of the list. 
dogs = ["Beagle", "Golden Retreiver", "Husky", "Black Lab"]
print("Here is the original list:")
print(dogs)
print("\nHere is the temporary sorted list:")
print(sorted(dogs))
print("\nAnd the original list again:")
print(dogs)

#Reverse a list (not alphabetically, just reverse the list chronologically)
dogs = ["Beagle", "Golden Retreiver", "Husky", "Black Lab"]
dogs.reverse()
print(dogs)
#Reversing the reverse. 
dogs.reverse()
print(dogs)

#Find length of a list using len() function:
dogs = ["Beagle", "Golden Retreiver", "Husky", "Black Lab"]
len(dogs)
print(len(dogs))
