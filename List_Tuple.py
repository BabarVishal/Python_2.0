# #List.......................
# marks = [1,2,3,4,5,6];
# print(marks)
# print(len(marks))
# print(marks[0])

# student = ["Vishal", 22, 1.3, "jalna"];
# print(student[0]);
# student[0] = 'babar';
# print(student);

# print(student[ : 3])
# print(student[ 0 : 3])
# print(student[ 0 : ])

# list method...........
list = [1,2,4,5,6,7,8]
# list.append(4); #add number to the last
# list.sort() #asc
# list.sort(reverse=True) #desc
# list.reverse() #reverse list
# list.remove() # remove the first occurence of index
list.pop(0) #remove element sat idx
# list.insert(1,1) #add values in list
print(list)


# Tuple................................
tup = (1,2,4,4);
print(type(tup))

#same slicing as list
#Tuple method
tup.count(1)
tup.index(2)