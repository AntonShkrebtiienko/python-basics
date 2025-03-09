from math import isclose
# variables
pocket = 5 # int
coefficient = 2.85 # float
sting_variable = 'just a string' # str
class SomeCustomClass : pass
fruits = ['Apples', 'Bananas', 'Grapes', 'Tomatoes'] # list
food = {'Bananas', 'Yoghurt', 'Bacon'} # set
workers : dict = {'name': 'Alan', 'age': 2} # dict, dictionary, dataset
instance = SomeCustomClass() # __main__.SomeCustomClass
a, b, c = 1, 2, 3 # this is called tuples unpacking method
x = y = z = 5 # also same value to different variables assigned
print(type(x)) # getting variable type
if (type(x), int):
    print(f'This int value is - {x}') # checking variable type and doing smth
print(a, b, c)
integer_number: int = 10 # type hints, could help me to assign static types
# print(type(food))
colour = (255, 0, 0) # tuple, represents an RGB colour
# naming
name = "Bob"
year_of_birth = 1992
isGay = True
age = 1
Age = 2
aGe = 3
AGE = 4 # all of them are different
# print(age, Age, AGE, aGe )
list = [1, 2 , 3, 4, 5, 6] # don't do this, you are shadowing the original object "list"
_timeout = 0 # non-public variable, uses only inside defining module
# class = 'Car' - cannot declare a variable from keywords names

match = True # this is soft keyword witch occurs to be reserved only in specific context

# variables discovered

# operators and expressions
print(2 * 3.12123 * 10)
s = 2
p = 1.1 + 2.2
print(isclose(p, 3.3)) # comparison of floating-point numbers is different
print(ord('A'), ord('a')) # Unicode code points of that str object type

isGay = True if True else False # ternary operator in Python
print(f'Am I gay?  - {isGay}!')
print(s is p, s is not p) # identity operator
print((boss_of_the_gym := True if isGay else False)) # walrus operator returns and assigns
# bitwise I don't understand yet

#conditional statements
# if ; if else; if elif else
gay = True
if  isGay:
    print('Yes, he is gay')
elif gay == isGay:
    print('Can I get your number, sussy?')
else:
    print('This time you passed, ok')

# dict.get method for dictionary check without if else
print(workers.get('name', 'WHo are you?'))

# loops
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    if cnt == 3 : print('Here is final count: ')
    print('Hello Geak')
else:
    print('Counter is bigger then 3')

n = 4
for i in range(0, n): # range from 0 to n-1
    print(i)

for letter in 'geeksforgeeks':
    #if letter == 'e' or letter == 's':
        # continue # returns the control to the begining of the loop
        # break
    pass
print('Current letter :', letter)

# match case statement

# name = input('Enter your name: ') # input from the User
#print('Hello, ', name)

def greet(name):
    """This function prints a greeting message"""
    print(f"Hello, {name}!") # docstring comment for documentation mostly

greet(name)

# TASKS
first_name: str = input('What is your first name? ').strip()

while not first_name:
    print('Error: This field cannot be empty!')
    first_name = input('What is your first name? ').strip()
print(type(first_name))

last_name: str = input('What is your last name? ').strip()
while not last_name:
    print('Error: This field cannot be empty!')
    last_name = input('What is your last name? ').strip()
print(type(last_name))

work_experience: int = int(input('What is your work experience in years? '))
while not work_experience:
    print('Error: This field cannot be empty!')
    work_experience = input('What is your work experience in years? ')
match work_experience:
    case n if n <= 2:
        print('Junior')
    case n if n > 2 and n <= 5:
        print('Middle')
    case n if n > 5 and n <= 8:
        print('Architect')
    case _:
        print(work_experience)
print(type(work_experience))

age: int = int(input('What is your age? '))
while not age:
    print('Error: This field cannot be empty!')
    age = input('What is your age? ')
print(type(age))

salary: float = float('{:.3f}'.format(float(input('What is your salary? ')) / 1000))
while not salary:
    print('Error: This field cannot be empty!')
    salary = '{:.3f}'.format(float(input('What is your salary? ')) / 1000)
print(type(salary))

is_on_project = input('Are u on project? (yes/no):').strip().lower() == 'yes' or input('Are u on project? (yes/no):').strip().lower() == 'no'
if is_on_project :
    print('Working!')
else:
    print('On the branch')

print(type(is_on_project))