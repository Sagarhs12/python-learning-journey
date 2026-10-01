print("Hello, World!")
name="Sagar" #string variable
age=24 #integer variable
price=99.99 #float variable

print("My name is", name, "and I am", age, "years old.")
print("The price of the product is", price, "dollars.")
print()
age2=age
print("My age is", age2, "years old.")
print()


#printing the type of variables
print(type(name))
print(type(age2))
print(type(age2))
print(type(price))
print()


name1="sagar"
name2='sagar'
name3='''sagar'''

print(name1)
print(name2)
print(name3)
print()


age3=24
old=False
a=None

print(type(age3))
print(type(old))
print(type(a))
print()


a=2
b=5

sum=a+b
sub=a-b
div=a/b
mul=a*b

print("Sum of a and b is:", sum)
print("Subtraction of a and b is:", sub)
print("Division of a and b is:", div)
print("Multiplication of a and b is:", mul)
print()


#comments in python are written using the hash symbol (#) for single-line comments and triple quotes (""" or ''') for multi-line comments.
""" Multi-line comment in python"""
#Hello

#Operators in python
#Arithmetic operators: +, -, *, /, %, **, //
print("Arithmetic operators in python:")
print()
x1=10
x2=3
result1=x1+x2
result2=x1-x2
result3=x1*x2
result4=x1/x2
result6=x1**x2
result7, result5 = divmod(x1, x2)
print("Addition of x1 and x2 is:", result1)
print("Subtraction of x1 and x2 is:", result2)
print("Multiplication of x1 and x2 is:", result3)
print("Division of x1 and x2 is:", result4)
print("Modulus of x1 and x2 is:", result5)
print("Exponentiation of x1 and x2 is:", result6)
print("Floor division of x1 and x2 is:", result7)
print()


#Relational operators: ==, !=, >, <, >=, <=
print("Relational operators in python:")
print()
x3=20
x4=10

result8=x3==x4
result9=x3!=x4
result10=x3>x4
result11=x3<x4
result12=x3>=x4
result13=x3<=x4


print("Is x3 equal to x4?", result8)
print("Is x3 not equal to x4?", result9)
print("Is x3 greater than x4?", result10)
print("Is x3 less than x4?", result11)
print("Is x3 greater than or equal to x4?", result12)
print("Is x3 less than or equal to x4?", result13)
print()


#Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
print("Assignment operators in python:")
print()
x5=55
xz=5
print("Initial value of x5:", x5)
print("Initial value of xz:", xz)

xz1=x5+xz #or xz1=x5+=xz
print("Value of xz1 after addition(x5+xz):",x5,"+",xz,"result:",xz1)
print("Value of x5 after addition:", x5)

xz2=x5-xz #or xz2=x5-=xz
print("Value of xz2 after subtraction(x5-xz):",x5,"-",xz,"result:",xz2)
print("Value of x5 after subtraction(after using -=):", x5)

xz3=x5*xz #or xz3x5*=xz
print("Value of xz3 after multiplication(x5*xz):",x5,"*",xz,"result:",xz3)
print("Value of x5 after multiplication(after using *=):", x5)

xz4=x5/xz #or xz4=x5/=xz
print("Value of xz4 after division(x5/xz):",x5,"/",xz,"result:",xz4)
print("Value of x5 after division(after using /=):", x5)

xz5=x5%xz #or xz5=x5%=xz
print("Value of xz5 after modulus(x5%xz):",x5,"%",xz,"result:",xz5)
print("Value of x5 after modulus(after using %=):", x5)
xz6=x5**xz #or xz6=x5**=xz
print("Value of xz6 after exponentiation(x5**xz):",x5,"**",xz,"result:",xz6)
print("Value of x5 after exponentiation(after using **=):", x5)

xz7=x5//xz #or xz7=x5//=xz
print("Value of xz7 after floor division(x5//xz):",x5,"//",xz,"result:",xz7)
print("Value of x5 after floor division(after using //=):", x5)
print()


#Logical operators: and, or, not
print("Logical operators in python:")
print()
#Not operator
#Give answer True if the operand is false, otherwise it will return False.
print(not True) #False
print(not False) #True
v1=60
v2=76
print(v1 <= v2)

print()
#And operator
#Give answer True if both the operands are true, otherwise it will return False.
value1=True
value2=True
print("the and answer operator: of","value1:",value1,"and",value2,"is:",value2,"then answer will be of value1 and value 2 is:",value1 and value2) #True

#Or operator
#Give answer True if any of the operands is true, otherwise it will return False.
value3=True
value4=False
print("the or answer operator: of","value3:",value3,"and",value4,"is:",value4,"then answer will be of value3 Or value 4 is:",value3 or value4) #True

print("OR Operator:",(value1==value2)or(value3>value4)) #True
print("AND Operator:",(value1==value2)and(value3>value4)) #False
print()

#Type conversion in python
print("Type conversion in python:")
print("There are two types of type conversion in python: Type Conversion and Type Casting.")
print("Type Conversion: It is the process of converting one data type to another data type automatically by python interpreter.")
print("Type Casting: It is the process of converting one data type to another data type manually by the programmer.")

n1=2
n2=3.5
n3="10"
sum1=n1+n2
print("The sum of n1", n1, "and n2", n2, "is:", sum1)#Using Type Conversion
print("The type of n3 is:", type(n3))
print("In Type Casting we can convert the string to integer using int() function.")
n4=int(n3)
print("The type of n4 is:", type(n4))
sum2=n1+n4
print("The sum of n1", n1, "and n4", n4, "is:", sum2)
number1=int("25")#converting string to integer
number2=4.25
print("number1=", number1, "and number2=", number2, "The sum of both is:", number1+number2)
print()


#Input in python
print("Input in python:")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old.")
print()
va=int(input("Enter a some value: "))
print(type(va),va)#