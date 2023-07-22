#     ........
    
# python collections:
#     1. list
#     2. tuple
#     3. set
#     4. Dictionary
    
#     .........

lst = [61,2,3,4,6,41]
print(lst)

var = type(lst)
print(var)

#slicing
var = lst[0]

lst[2]=45
var=lst[2]
var=lst

# var = lst[1:4]
var =len(lst)
print(var)

#adding element in list
list=[32,2,5,8,15,25]
list.append(100)
print(list)

#adding according to position
list.insert(1,100)
print(list)

#remove element from list
list.remove(5)
print(list)

#pop funtion- remove element from last in list
list.pop()
print(list)

#del function remove from any position in list
del list[3]
del list
print(list)

#clear funtion 
list.clear()
var = list
print(var)



