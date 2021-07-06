num1 = 42 #saved a num as an int, variable declaration
num2 = 2.3 #saved a num as a float, variable declaration
boolean = True #Boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initalize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary initalize
fruit = ('blueberry', 'strawberry', 'banana') #tuple initalize
print(type(fruit)) #type check
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #change value
print(fruit[2]) #access value
"""
if else conditional that will print("It's lower")
because num1 is 42
"""
if num1 > 45: 
    print("It's greater")
else:
    print("It's lower")

"""
if else conditional
uses the length of the string named earlier
the length is 11 
so it will print out "Just right!"
"""
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop start
    print(x)       #for loop what to do
for x in range(2,5): #for loop start and stop
    print(x)         #for loop what to do
for x in range(2,10,3): #for loop start, stop, and how to increment
    print(x)            #for loop what to do
x = 0           #x for while loop below
while(x < 5):   #start of while loop, also when to stop
    print(x)    #while loop what to do
    x += 1      #increment while loop

pizza_toppings.pop() #delete last value
pizza_toppings.pop(1) #delete value at index 1

print(person) #access all of person dictionary
person.pop('eye_color') #delete value
print(person) #access all of person dictionary

for topping in pizza_toppings: #start of for loop
    if topping == 'Pepperoni': #if statement
        continue #continue with for loop
    print('After 1st if statement') #end of 1st if
    if topping == 'Olives': #if statement
        break #break out of for loop

def print_hello_ten_times(): #function
    for num in range(10): #for loop start and stop
        print('Hello') #what to do in for loop

print_hello_ten_times() #calling function

def print_hello_x_times(x):#function w/argument
    for num in range(x):#for loop start and stop
        print('Hello')#what to do in for loop

print_hello_x_times(4)#calling function and passing argument of 4

def print_hello_x_or_ten_times(x = 10): #calling function w/argument for for loop
    for num in range(x): #for loop start and end
        print('Hello') #for loop what to do

print_hello_x_or_ten_times() #call function and runs as shown
print_hello_x_or_ten_times(4) #call function changes for loop argument to 4


"""
Bonus section
"""

# print(num3) --name error
# num3 = 72 
# fruit[0] = 'cranberry' --tuple error-type error
# print(person['favorite_team']) --key error
# print(pizza_toppings[7]) --index error
#   print(boolean) --indent error
# fruit.append('raspberry') --tuple error-- cant append
# fruit.pop(1)--tuple error-- can't delete