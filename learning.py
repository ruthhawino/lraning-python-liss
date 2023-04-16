  

# lis comrehension using for-loop

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# 
# // we can create new list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



# we can acces each element in alist using indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# we can add item from a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# //we can remove item from a list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# list can be be joined by creating new list

list1 = ["a", "b", "c"]
list2 = [67, 38, 43]

list3 = list1 + list2
print(list3)

# //list can be sorted
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)