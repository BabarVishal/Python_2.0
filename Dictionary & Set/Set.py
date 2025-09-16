#Set is collection of unordered items;
#They are immutable and Each element in set be Unique;
# set => element => immutable

nums = {1,2,3,4,5,5,6,7};
print(nums);
print(len(nums))

Collection = set();  #Empty Set

#Set Methods........
Collection.add(22);
Collection.remove(22);
Collection.clear(); #empties the set
Collection.pop(); # remove the random value
Collection.union() #Combines both set values and return new
Collection.intersection() #Comman Values in set
print(Collection);
