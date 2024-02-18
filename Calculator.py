num1=int(input("Enter the number1 to perform any operation:"))
num2=int(input("Enter another number2 to perform the operation"))

operator=input("Enter the operator to perform any operation on numbers (+, -, *, /, %):")

if(operator== '+'):
   add= num1 + num2
   print(f"The additon of {num1} and {num2} is{add}")
elif(operator=='-'):
    sub=num1-num2
    print(f"The asubtraction of {num1} and {num2} is{sub}")
elif(operator=='*'):
    mul=num1*num2
    print(f"The multiplication of {num1} and {num2} is{mul}")
elif(operator=='/'):
    div=num1/num2
    print(f"The division of {num1} and {num2} is{div}")
elif(operator=='%'):
    mod=num1%num2
    print(f"The modulus of {num1} and {num2} is {mod}")
else:
    print("Please select an appropriate operator or check the input numbers!!!")
