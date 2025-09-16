my_List = ["Vishal", "Shubz", "om", "Onkar", "Shuz"];

a = my_List[1];
b = len(my_List);

my_List[1] = "mayur";
print(my_List);

#Slicing
c = my_List[1:4];
print(c);

#List Methods
List = [1,2,3,4,10,5,6];
print(List);
List.append(7); #addElementInTheEdd
print(List);
List.sort(); #AsendingOrder Eg:1,2,3,...
print(List);
List.sort(reverse=True) #DecendingOrder Eg:5,4,3,2,....
print(List);
List.reverse(); #reverseList
print(List);
List.insert(0,100); #InsertElementInIndex
print(List);
List.remove(1);
List.pop(1) #RemoveElementAtIndex