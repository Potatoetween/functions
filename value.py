def absolute(number):
    if number>=0:
        return number
    else: 
        return -number
number=int(input("enter a number"))
print("the absolute value of",number,"is",absolute(number))