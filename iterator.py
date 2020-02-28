my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)
print(my_iter)

## iterate through it using next() 

#prints 4
print(next(my_iter))

print(my_iter.__next__())
