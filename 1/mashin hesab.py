number1 = int(input("Lotfan adade aval ra vared konid : "))
number2 = int(input("Lotfan adade dovom ra vared konid : "))

operator = input("operator ra vared konid (+,-,*,/) : ")

if(operator == "+"):
    print(number1 + number2)
if(operator == "-"):
    print(number1 - number2)
if(operator == "*"):
    print(number1 * number2)
if(operator == "/"):
    print(number1 / number2)
else:
    print('fazet chie?')