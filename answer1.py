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
