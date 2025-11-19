import math
def add(*args): 
    """Adds two numbers"""
    return sum(args)
def subtract(*args):
    """Subtracts two numbers"""
    print("Reached subtract function")
    #result = first arg 
    #for each argument after the first arg 
        #subtract that number from the result and store it as the new result 
    #return result
    result = args[0]
    for num in args[1:]:
        result = result - num

    return result 

def mult(*args): 
    result = math.prod(args)

    return result 

def div(*args): 
    result = args[0]
    for num in args[1:]: 
        if num != 0:
            result = result/num      
            return result      
        else: print("Error")

#interface
operation = input(f"which operation would you like to input\n insert operation:")
numbers = input("What numbers would you like to execute the operation on?  insert number or list of numbers:")

#For numbers, it is being stored as a string but it needs to be passed as the argument for the functions which require list "*args" meaning i have to create another variable to split the string into a list
split_numbers = numbers.split() 

op = operation.strip().lower()
if op == "divide": 
    print(div(*split_numbers))
elif op == "multiply": 
    print(mult(*split_numbers)) 
elif op == "divide": 
    print(mult(*split_numbers)) 
elif op == "add": 
    print(add(*split_numbers))
elif op == "addition": 
    print(add(*split_numbers))
elif op == "subtract": 
    print(subtract(*split_numbers))

#debugging: 
print(numbers) 
print(type(numbers))
