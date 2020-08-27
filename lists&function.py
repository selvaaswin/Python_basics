#LIST
names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
names[1] = "kalai"
print(names[1:])
"""above program are list and how to change a value and how to 
print a specific, target from a list"""
# comments begining with ( """ ) also has indetation errors

#list function

names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names.extend(numbers)    #used to add another list to an existing list
print(names)

names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names.append("vignesh")   #append is used to add a value to the list
print(names)

names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names.insert(1,"abishek")     #insert is used to insert a value in the given place holder
print(names)


names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names.remove("sanjay")  #remove is used to remove a selected value
print(names)


names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names.clear() #clear is used to clear all the values
print(names)

names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names.pop()    #this is used to pop a value from the end
print(names)

names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
print(names.index("giri"))  #this function is used to index the given value

names = ["aswin" , "selva" , "sanjay" , "giri" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
print(names.count("giri"))    #counts the number of times the value is repeated

names = ["aswin" , "selva" , "sanjay" , "giri" , "abishek" , "kalai",  "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names.sort()  #used to sort the list in ascending order
numbers.sort()  #this function can also sort numbers
print(names)
print(numbers)

names = ["aswin" , "selva" , "sanjay" , "giri" , "abishek" , "kalai",  "sangeeth"]
numbers = [5, 6, 8, 3, 0]
names2 = names.copy()  #this function is used copy values from one list to another
numbers2 = numbers.copy()  #same as above
print(names2)
print(numbers2)

names = ["aswin" , "selva" , "sanjay" , "giri" , "sangeeth"]
numbers = [5, 6, 8, 3, 0]
print(names[3])