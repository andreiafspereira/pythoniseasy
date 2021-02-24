"""
PIRPLE PYTHON IS EASY
Homework #4: Lists
File name: listhw4.py
Description: Function that adds unique elements to an empty list.
             The function returns True if the added element is unique and returns false if the element is repeated
"""

myUniqueList = []
myLeftovers = []

def addToMyList(a):
    if a not in myUniqueList:
        myUniqueList.append(a)
        print('True')
    else:
    	myLeftovers.append(a)
    	print('False')


# add an integer student ID to myUniqueList
studentID = 2021
addToMyList(studentID)

# add a string student name to myUniqueList
studentName = "Andreia"
addToMyList(studentName)

# add another integer student ID to myUniqueList
studentID = 2001
addToMyList(studentID)

# add another string student name to myUniqueList
studentName = "Francisco"
addToMyList(studentName)

# add the same studentID name to myUniqueList - it should go to myLeftovers
studentID = 2021
addToMyList(studentID)

# add the same studentName - it should go to myLeftovers
studentName = "Andreia"
addToMyList(studentName)

print(myUniqueList)
print(myLeftovers)