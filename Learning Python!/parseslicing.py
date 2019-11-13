#Create a text (could be input) and slice/parse the text. Specifically grab the domain of the email

text = "Please email any concerns you may have to administration@thebatcave.com  and we will response accordingly. "


at_pos = text.find("@") #Find the postion of @ and set to variable. 
print(at_pos)#positon 56. 

space_pos = text.find(" ",at_pos) #find the first space starting at the at_pos variable
print(space_pos)#postionin 71

parse = text[at_pos:space_pos] #space_pos passed here does NOT include the space, but up to the space. 
print(parse)
								 