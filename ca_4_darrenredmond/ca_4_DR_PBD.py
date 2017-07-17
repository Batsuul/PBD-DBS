

#----------------------------------------------------------------
# 1    add two numbers and return the result
#----------------------------------------------------------------
'''def Addition (number1, number2) :
	return number1 + number2
	
a = [66.25, 333, 333, 1, 1234.5]
	
number1 = int(raw_input("enter first number:"))
number2 = int(raw_input("enter second number:"))
number3 = Addition(number1, number2)
print ("The addition of two number is :"+ str(number3))'''



'''number1 = int(raw_input("enter first number:"))
number2 = int(raw_input("enter second number:"))
add = lambda number1, number2 : number1 + number2'''

#please not my original functions above work individually 
#print add(number1, number2)

mylist=[42,22,13,3,6,8,8789,12,17,6787,999,2323,67,43,34,79,45,4556, 787]

list=reduce(lambda x,y:x+y,mylist)

print list



#----------------------------------------------------------------
# 2  subtract second number from the first number
#----------------------------------------------------------------

'''def subtract (number1, number2):
	return number1 - number2
	
number1 = int(raw_input("please enter your first number:"))
number2 = int(raw_input("please enter your second number:"))
number3 = subtract(number1, number2)
print ("The result of subtraction of two number is :"+ str(number3))'''

list_minus = [2,3,5,7,78,89,07,3,412,565,234,23,46,132,89]
formula =[5-x for x in list_minus]
print formula
	
#----------------------------------------------------------------
#  3   multiply first number by the second and give the result
#----------------------------------------------------------------	
'''def multiply (first, second):
	return first * second	

number1 = int(raw_input("please enter your first number:"))
number2 = int(raw_input("please enter your second number:"))
number3 = multiply(number1, number2)
print ("The result of multification  of two number is :"+ str(number3'''

list_of_multilpy = [1,2,33,4,5,6,35,34,22,20,45,46,25,27,29,28,87,43]
result = [4*x for x in list_of_multilpy]
print result
	
#----------------------------------------------------------------
# 4   divide first number by the second number and get result
#----------------------------------------------------------------
	
'''def divide (first,second):
	return first / second
		
number1 = int(raw_input("please enter your first number:"))
number2 = int(raw_input("please enter your second number:"))
number3 = divide(number1, number2)
print ("The result of division of two number is :"+ str(number3))'''

list = [23,234,45,1,4,5465,1232,45,1334,56567,23123,688,12323,13,415,98]
result = filter(lambda x: x / 2, list)
print result
result = filter(lambda x: x / 2 == 0, list)
print result





#----------------------------------------------------------------
#   5 power of the number
#----------------------------------------------------------------	
	
'''def Pow (base, power):
	return  base**power
	

		
#base = int(raw_input("please enter your first number to calculate power:"))
#power = int(raw_input("please enter your second number to calculate power:"))
#print ("The result of Power of the numbers is :"+ str(printpower))'''


base = int(raw_input("please enter your first number to calculate power:"))
power = int(raw_input("please enter your second number to calculate power:"))
# lambda function to calculate base number by power
Pow = lambda base, power : base ** power

print ("The result of power of the number is :" , (Pow(base,power)))        
#----------------------------------------------------------------
# 6  square
#----------------------------------------------------------------	
	
def square (number):
	return number ** 2

user_input	= int(raw_input("please enter your number to get the square of it: "))

number = square(user_input)

print ("the square result of your given number is :"+ str(number))

Lists = [1, 2, 3, 4, 5]
square = []
for x in Lists:
	square.append(x ** 2)

	
print square





#----------------------------------------------------------------
# 7  cube
#----------------------------------------------------------------	
	
def cube (num):
	return num**3

user_input = int(raw_input("please enter  a number to get cube of it: "))

number = cube(user_input)
print ("the cube of your given number is as follow: "+str(number))

Lists = [1, 2, 3, 4, 5]
cube = []
for x in Lists:
	cube.append(x ** 3)

	
print cube
		
#----------------------------------------------------------------
# 8 square root
#----------------------------------------------------------------
def squareRoot(n):
	if n > 0:
		return n ** 0.5
	elif n == 0:
		return (0)
	else:
		return ("inf")
		
number = squareRoot(user_input)
user_input = int(raw_input("please enter the number to get the square root of it:"))
print ("this is the squareRoot of the number you are looking for :" +str(user_input** 0.5))  

#----------------------------------------------------------------
#  9 factorial of the number
#----------------------------------------------------------------
'''def factorial(n):
	if n > 1:
		return n * factorial(n- 1)
	if n < 0:	
		return 'inf'
	return 1
	
user_input = int(raw_input("please enter a number you wish to get factorialof: "))
factorial_of_user_input = factorial(user_input)
print factorial_of_user_input'''




 
user_input=int(raw_input("please enter the number you wish to calculate factorial of"))
print(lambda b: (lambda a, b: a(a, b))(lambda a, b: b*a(a, b-1) if b > 0 else 1,b))(user_input)

#----------------------------------------------------------------
#  10 modulo
#----------------------------------------------------------------
'''def modulo(number1, number2):
	return number1%number2

number1 = int(raw_input("please enter the first number :") )
number2 = int(raw_input("please enter the second number :") )
number3 = modulo(number1, number2)
print ("your given number's result is  :" +str(number3))'''

filter_my_list = [23,2,34,21,35,677,78,989,12,14,3,43,3433,4367,46585678,2453]
result = filter(lambda x: x % 2, filter_my_list)
print result

result = filter(lambda x: x % 2 == 0, filter_my_list)
print result




'''user_input = (int(raw_input("please enter any number betbeen the of range(1, 100)")))

for i in range(2, 50): 
     user_input = filter(lambda x: x % i, user_input)

print user_input'''
    
	

 

	
	
	
	
	

	
	
	