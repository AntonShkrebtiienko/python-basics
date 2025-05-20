# Task 1
storage: list = []

def add_new_developer(storage: list,
                      id: int,
                      first_name: str,
                      last_name: str,
                      work_experience: int,
                      salary: float,
                      currency: str = 'USD',
                      **kwargs) -> None:

    developer: dict = {
                       'id': id,
                       'first_name': first_name,
                       'last_name': last_name,
                       'work_experience': work_experience,
                       'salary': salary,
                       'currency': currency,
                       'kwargs': kwargs
                       }

    for key, item in developer.items():
        if key and item:
            developer.pop('kwargs')
            storage.append(developer)
            break
        else:
            print('not')

add_new_developer(
                   storage, id = 1,
                   first_name = 'Adam',
                   last_name = 'Smasher',
                   work_experience = 7,
                   salary = 5.8
)

add_new_developer(
                  storage,
                  id =2, first_name ='Johny',
                  last_name = 'Silverhand',
                  work_experience = 2,
                  salary = 1.5,
                  age=27, department='DevOps'
)

add_new_developer(
                  storage,
                  id =3, first_name ='Panam',
                  last_name = 'Palmer',
                  work_experience = 5,
                  salary = 170.5,
                  currency ='UAH',
                  projects=['Project1', 'Project2', 'Project3']
)

add_new_developer(
                  storage,
                  id =4, first_name ='Jackie',
                  last_name = 'Welles',
                  work_experience = 3,
                  salary = 2.7,
                  currency = 'EUR'
)

print(f'storage: {storage}')

#Task 2

def get_developer_by_id(storage: list, id: int) -> dict | None:
    for item in storage:
        if item['id'] == id:
            return item
    return None



get_developer_by_id(storage, 1)
get_developer_by_id(storage, 3)

# Task 3

def update_developer_by_id(storage: list, dev_id: int, **kwargs) -> None:
    found_dev: dict = get_developer_by_id(storage, dev_id)
    new_id: int = kwargs.get('id')

    if any(item.get('id') == new_id for item in storage):
        print('Developer with specified id already exist')
        pass
    else:
        found_dev.update(kwargs)
        print('updated storage: ', storage)


update_developer_by_id(storage, 1, id=2)
update_developer_by_id(storage, 4, work_experience=4, currency='USD', age=24)

# Task 4
def remove_developer_by_id(storage:list, id:int) -> None:
    found_dev = get_developer_by_id(storage, id)

    if found_dev:
        storage.remove(found_dev)

remove_developer_by_id(storage, 3)

# Task 5
def add_projects(developer: dict, *args) -> None:
    if 'projects' not in developer:
        developer['projects'] = list(args)
    elif isinstance(developer['projects'], list):
        developer['projects'].extend(args)
    else:
        print('Developer already has "projects" key and its not a list type')

add_projects(storage[0], 'Smart House', 'Stream Platform',
                                'Audio Translator', 'Tron', 'LOL' )
print(storage)

# Task 6

storage = sorted(storage, key = lambda dev: dev['work_experience'])
print(f'storage: {storage}')

experienced_devs = list(filter(lambda dev: dev['work_experience'] > 3, storage))
print(f'storage Exp: {experienced_devs}')

usd_to_uah = 41.47

converted_storage = list(map(
    lambda dev: {
    **dev,
    'salary_uah': round(dev['salary'] * usd_to_uah, 2)
    },
    storage
))
print(f'converted_storage: {converted_storage}')