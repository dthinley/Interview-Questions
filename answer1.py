#define a list with strings
fruits = ["apple", "banana", "orange", "mango"];

# defines a function that takes in a list and return unordered html list
def htmlList (list):
    ulList = "<ul>"
 #iterates through a list and returns a list item
    for i in list:
       ulList += "<li>" + i + "<li>"
       ulList += "<ul>"
 
    print (ulList)
 
htmlList(fruits)


# If the original list was a user input, empty list can be created
# to store the strings. Next create while loop that takes user input and break the loop. 
# We can then append the user input into the list and call each string on the 
# list to insert it between <li></li>
