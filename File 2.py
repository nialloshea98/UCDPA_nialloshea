import numpy as np

#Creating a 2D numpy array and printing it
a = np.arange(16).reshape((4, 4))
print(a)

#Understanding the data
print(a.shape)
print(a.dtype.name)
print(a.size)


print(a[0, 3]) #Selcting a specific value in the array
print(a[2, :]) #printing the entire third row
print(a[:, 2]) #printing the entire third column

#Basic numpy maths
print(np.mean(a))
print(np.median(a))
print(np.std(a))

#Created the school dictionary with different populations of schools
school = {"School1": 845, "School2": 348, "School3": 965, "School4": 457, "School5": 741}

#printing the coresponding value for School3
print(school["School3"])

#Adding a new vaule
school["School6"] = 354
print((school))

#Deleting a value
del(school["School6"])
print((school))

#checking if there is a school 7
print('School7' in school)
