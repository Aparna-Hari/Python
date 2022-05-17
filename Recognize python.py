num1 = 42
num2 = 2.3 #Initializing variables
boolean = True #boolean type
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list of toppings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary with keys and values
fruit = ('blueberry', 'strawberry', 'banana') #tuples which are immutable
print(type(fruit)) #tuple type
print(pizza_toppings[1]) # outputs sausage
pizza_toppings.append('Mushrooms') # ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives' ,'Mushrooms']
print(person['name']) # dictionary[key] outputs value associated with key -John
person['name'] = 'George' #Assigning value 'George' to name  person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person['eye_color'] = 'blue' # {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False ,'eye_color':'blue' }
print(fruit[2]) #banana

if num1 > 45:
    print("It's greater") # if-else statement
else:
    print("It's lower")

if len(string) < 5: # syntax for length of string is len(string) and we are using, if,elif and else statements
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop through the list of elements until index 4,excludes 5
    print(x)
for x in range(2,5): # for loop starts at index 2 and stops at index 4,excludes 5
    print(x)
for x in range(2,10,3): # for loop starts at index 2 and stops at index 9,excludes 10 and increments by 3
    print(x)
    print(x)
x = 0
while(x < 5): # keep looping until x is 4
    print(x)
    x += 1

pizza_toppings.pop() # ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', ]
pizza_toppings.pop(1) # ['Pepperoni', 'Jalepenos', 'Cheese', ]

print(person)      #{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False ,'eye_color':'blue' }
person.pop('eye_color') # {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
print(person)

for topping in pizza_toppings: #['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives' ,'Mushrooms']
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #print 0 through 9, i.e 10 times
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)