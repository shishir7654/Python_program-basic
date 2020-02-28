odd_square = [x **2 for x in range(1,11) if x%2 ==1]
print(odd_square)


# for understanding, above generation is same as, 
odd_square = [] 
for x in range(1, 11): 
    if x % 2 == 1: 
        odd_square.append(x**2) 
print( odd_square)


# below list contains power of 2 from 1 to 8 
power_of_2 = [2 ** x for x in range(1, 9)] 
print (power_of_2 )


string = "my phone number is : 11122 !!"
  
print("\nExtracted digits") 
numbers = [x for x in string if x.isdigit()] 
print (numbers )
  
