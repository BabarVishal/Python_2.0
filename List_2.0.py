list = [1,2,3,4,5,6,7]

list.append(8)
list.insert(0, 11)
list.pop(1)
list.sort()
list.sort(reverse=True)
list.reverse()

print(list)

list2 = ['Vishal', 22, 22.22, 'Babar'];

print(list2[ : 3])
print(list2[0 : ])
print(list2[ -3 : ])
print(list2[1])


List3 = ['vishal', 'om', 'shubz', 'mayur', 'Kru']
print(len(List3))
print(type(List3))

if 'Kru' in List3:
    print('Good Day')

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


data = ['vishal', 'om', 'shubz', 'mayur', 'chetan', 'kapur']
data2 = []

for x in data:
   if 'vishal' in x:
      data2.append(x)

print(data2)