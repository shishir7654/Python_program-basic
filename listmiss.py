list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]


print("Mission values in second list:",(set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1))) 


print("Missing values in first list:", (set(list2).difference(list1))) 
print("Additional values in first list:", (set(list1).difference(list2))) 
