#Set- dont want repeate element you can use set

s1={34,2,3,4,5,5,5,5,5,5,5,5,7,9,8,6,23}
print(s1)

s1.add(3333)
print(s1)

#add multiple element
s1.update([12,33,23,45,54,35,53])
print(s1)
print(len(s1))

#remove element only that element which is in list
s1.remove(6)
print(s1)

#discard- without any error if value in list 
# it will remove otherwise without error print
s1.discard(23435)
print(s1)

# like list you can add: .pop, .clear, del,and....
# intersection, union