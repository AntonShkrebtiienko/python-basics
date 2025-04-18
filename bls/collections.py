import copy
# Task 1

developer: dict = {}

while True:
    first_name: str = input('What is your first name? ').strip()
    if len(first_name) > 0:
        developer.setdefault("first name", first_name)
        break
    else:
        print('Input your name, please :)')
    continue

while True:
    last_name: str = input('What is your last name? ').strip()
    if len(last_name) > 0:
        developer.setdefault("last name", last_name)
        break
    else:
        print('Input your last name, please :)')
    continue

while True:
    work_experience = input('What is your work experience in years? ')
    try:
        work_experience = int(work_experience)
        developer.setdefault("work experience", work_experience)
        break
    except ValueError:
        if not work_experience:
            break
        else:
            print('Input an integer value of your work experience')
    continue

while True:
    age = input('What is your age? ')
    try:
        age = int(age)
        developer.setdefault("age", age)
        break
    except ValueError:
        if not age:
            break
        else:
            print('Input an integer value of your age')
    continue

while True:
    salary_input = input('What is your salary? ')
    try:
        salary_converted = int(salary_input) / 1000
        salary = round(salary_converted, 3)
        developer.setdefault("salary", salary_converted)
        break
    except ValueError:
        print('error')
    continue

while True:
    try:
        is_on_project = input('Are u on project? (yes/no):').strip().lower() == 'yes'
        developer.setdefault("is on project", is_on_project)
        break
    except ValueError:
        print('error')
    continue


print(
    developer["first name"] + " | " +
    developer["last name"] + " | " +
    str(developer["work experience"]) + " | " +
    str(developer["age"]) + " | " +
    str(developer["salary"]) + " | " +
    str(developer["is on project"])
)
print(
    "{} | {} | Experience: {} yrs | Age: {} | Salary: ${:.3f} | On project: {}".format(
        developer['first name'],
        developer['last name'],
        developer['work experience'],
        developer['age'],
        developer['salary'],
        developer['is on project']
    )
)
print(
    f"{developer['first name']} | {developer['last name']} | "
    f"Experience: {developer['work experience']} yrs | "
    f"Age: {developer['age']} | "
    f"Salary: ${developer['salary']} | "
    f"On project: {developer['is on project']}"
)

for key, value in developer.items():
    print(f"key={key.upper()}; value=<{value}>")

# Task 2
projects = [f"Project{i}" for i in range(1,6,1)]
developer.setdefault("projects", projects)

for i in range(len(developer["projects"])) :
    if i % 2 == 0 and i > 0:
        print(f"Index={i}; Project={developer["projects"][i]}")

for i, x in enumerate(developer["projects"]):
    if i % 2 == 0 and i > 0:
        print(f"Index={i}; Project={developer["projects"][i]}")

# Task 3
developer_copy = copy.deepcopy(developer)
developer_copy["projects"].append("Project6")
developer["projects"].pop(0)
developer["projects"] = set(developer["projects"])
developer_copy["projects"] = set(developer_copy["projects"])

print("Union:", developer["projects"] | developer_copy["projects"])
print("Intersection:", developer["projects"] & developer_copy["projects"])
print("New dev difference:", developer_copy["projects"] - developer["projects"])