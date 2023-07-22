name="Ravi"
name='''Ravi
is a good boy'''
print(name)
print(name[0])

#slice string
print(name[1:3])

# strip for remove space
name= "Ravi"
print(name.strip())

# Know length of string
print(len(name))

#upper /lower
var = name.lower()
var = name.upper()
print(var)

#replace funtion
var =name.replace("R", "s")
print(var)

#remove comma to blank
name="Ravi, Shubham, mani"

var=name.replace(",","")
print(var)


stri1= "This is a "
stri2 ="This is not a"
name="Ravi"
print(stri1+stri2)
print(stri1+name)

#template format

name1="Ravi"
name2= "Mani"
temp= "This is a {} and he is a good boy named {}".format(name1,name2)
print(temp)

temp= "This is a {0} and he is a good boy named {1}".format(name1,name2)
print(temp)

temp = f"this is a {name1} and he is a good boy {name2}"
print(temp)



