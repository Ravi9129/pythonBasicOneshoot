#Tuple- you can not change tuple items
a =("Ravi","mani", "Shubham")
var = a
var=type(a)
#we can not change the value of tuple
# a[0] = "Avi"
print(var)

a=list(a)
var=type(a)
a[0]= "Avi"
print(var)

