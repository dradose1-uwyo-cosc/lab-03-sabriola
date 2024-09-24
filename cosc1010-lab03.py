#Serina Abriola
#UWYO COSC 1010
#September 22, 2024
#Lab 03
#Lab Section: 16
#Sources: Lecture 5 and 6


# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
list_states = ["Wyoming", "Colorado", "Montana"]

#print the entire list
print(list_states)

#now print the first element in the list
print(list_states[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(list_states[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{list_states[1].upper()} is south of {list_states[0].upper()}")


print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
list_states.append("Washington")
list_states.append("Oregon")
list_states.append("California")
print(list_states)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
list_states[-2] = "Maine"
print(list_states)

#Insert the state Texas to be the third element in the list, again printing your list
list_states.insert(2, "Texas")
print(list_states)

#Using the `del` statement remove the fourth item from the list, print your list 
del list_states[3]
print(list_states)

#Remove Texas using its value, print the list
list_states.remove('Texas')
print(list_states)


print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(list_states))
print(list_states)

#Permanently sort your list in reverse order, printing it out
list_states.sort(reverse = True)
print(list_states)

#Using the reverse method reverse the list and print it
list_states.reverse()
print(list_states)
