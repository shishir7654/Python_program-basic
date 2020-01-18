# Python program to display all the prime numbers

lower = 100
upper = 1000

print("Prime number between ",lower, "and", upper, "are:")

for num in range(lower, upper+1):

    if num > 1:
        for i in range(2,num):
            if ( num% i)==0:
                break
        else:
            print (num)
