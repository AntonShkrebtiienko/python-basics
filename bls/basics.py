# TASKS 1 and 2
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

is_on_project = input('Are u on project? (yes/no):').strip().lower() == 'yes'
if is_on_project :
    print('Working!')
else:
    print('On the branch')

print(type(is_on_project))

# TASK 3

developers_counter = 0

while (developers_counter < 5) :
    developers_counter += 1


    while True:
        first_name: str = input('What is your first name? ').strip()
        if first_name.isdigit():
            print('Input valid string value of your first name')
        else:
             break

    if not first_name :
        continue

    while True:
        last_name: str = input('What is your last name? ').strip()
        if last_name.isdigit():
            print('Input valid string value of your last name')
        else:
            break

    if not last_name:
        continue

    while True:
        work_experience = input('What is your work experience in years? ')
        try:
            work_experience = int(work_experience)
            break
        except ValueError:
            if not work_experience:
                break
            else:
                print('Input an integer value of your work experience')
                continue

    if not work_experience or int(work_experience) < 2:
        continue

    while True:
        age = input('What is your age? ')
        try:
            age = int(age)
            break
        except ValueError:
            if not age:
                break
            else:
                print('Input an integer value of your age')
                continue

    if not age:
        continue

    while True:
        salary = '{:0.3f}'.format(float(input('What is your salary? ')) / 1000)
        try:
            salary = float(salary)
            break
        except ValueError:
            print('error')
            continue

    if not salary or salary >= 5.000:
        continue

    is_on_project = input('Are u on project? (yes/no):').strip().lower() == 'yes'

    if work_experience == 3 and salary == 2.500:
        print('Hired')
        break

    print(developers_counter, first_name, last_name, work_experience, age, salary, is_on_project)
else :
    print('Still in search')
