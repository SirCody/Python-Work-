#From Python Crash Course#

#Strings, Concatenate strings, edit case

#Edit the case of a string
name = "josh clark"
#change the string to title case and print:
print(name.title())
#Change to all upper case and print:
print(name.upper())
#Change to all lower case and print:
print(name.lower())

#Concatenating Strings.
first_name = "josh"
last_name = "clark"
full_name = first_name + " " + last_name
#Concatenating string, but also calling the variable full_name and title casing it:
print("Hello " + full_name.title() + "!")
#Assign the same as above but to a variable, and print only the variable. 
message = "Hello, " + full_name.title() + "!"
print(message)


#Adding and removing whitespace:
print("Python")
#this adds a tab
print("\tPython")
#this adds a new line:
print("Python:\nRuby:\nJava:\nC++:")
#this combines both:
print("\nLanguages:\n\tPython\n\tRuby\n\tC++")
#removing white space.
best_language = 'python '
#printing the variable with the space to the right. 
print(best_language)
#.rstrip "strips" the right side space, and print that variable
print(best_language.rstrip())
#edits the variable to permanently remove the whitespace. 
best_language = best_language.rstrip()
print(best_language)
#Playing with left strip and stip. Strip removes all whitespace. 
bestlanguage = "  python"
print(bestlanguage.lstrip())
print(bestlanguage) #this produces "python" with no space
print(bestlanguage.strip()) #same result. 
bestlanguage = bestlanguage.strip()
print(bestlanguage) #same result

### Try yourself! pg 29 of Python Crash Course###
#Testing some of the above learning techniques for whitespace, title and concatenation:
#2-3:
name = "Lauren"
print("Hello, " + name + "!")
#2-4:
name = "lauren"
print(name.title())
print(name.upper())
print(name.lower())
#2-5:
print('Albert Einstein once said, "A person who never made a mistake never tried anything new"')
#2-6:
famous_person = "Albert Einstein"
message = famous_person + ' once said, "A person who never made a mistake never tried anything new"'
print(message)
#2-7:
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


