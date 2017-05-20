import functions
print("Enter one number")
print("1 for sum")
print("2 for mul")
print("3 for sub")
print("4 for div")

op=int(input("Enter now: "))
number1=int(input("enter first number: "))
number2=int(input("enter second number: "))
if (op == 1):
    print("Sum")
    functions.sum(number1,number2)
elif (op == 2):
    print ("mul")
    functions.mult(number1, number2)
elif (op == 3):
    print("sub")
    functions.subs(number1, number2)
elif (op == 4):
    print("div")
    functions.division(number1, number2)
else:
    print("Incorrect number")