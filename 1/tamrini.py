number1 = int(input("Lotfan adade aval ra vared konid : "))
number2 = int(input("Lotfan adade dovom ra vared konid : "))

if number1 or number2 ==str:
    print('adad lotfan')


operator =input("operatore morede nazar ra vared konid(*,/,+,-): ")

if(operator == "+"):
    print(number1+number2)
if(operator == "-"):
    print(number1-number2)
if(operator == "/"):
    print(number1/number2)
if(operator == "*"):
    print(number1*number2)
else:
    print("FAGHAT ADAD")