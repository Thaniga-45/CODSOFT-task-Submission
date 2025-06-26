print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
operation = int(input("choose an operation:"))

if(operation in [1,2,3,4]):
    num1 = int(input("enter a first number:"))
    num2 = int(input("enter a second number:"))
    
    if(operation == 1):
        result= num1 + num2
    elif(operation == 2):
        result = num1- num2
    elif(operation == 3):
        result = num1 * num2
    elif(operation == 4):
        result = num1 // num2
    
else:
    print("Invalid operation entered")
print("the result of the operation is {} :".format(result))
