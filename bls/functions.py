# Task 1
storage: list = []

def add_new_developer(storage: list,
                      id: int,
                      first_name: str,
                      last_name:str,
                      work_experience: int,
                      salary:float,
                      currency: str = 'USD',
                      **kwargs) -> None:

    developer: dict = {'id': id,
                       'first name': first_name,
                       'last name': last_name,
                       'work experience': work_experience,
                       'salary': salary,
                       'currency': currency,
                       'kwargs': kwargs
                       }

    for key, item in developer.items():
        if key and item:
            #print('got u', item)
            developer.pop('kwargs')
            storage.append(developer)
            break
        else:
            print('not')

add_new_developer(storage, 1, 'Adam',
                  'Smasher',7, 5.8)

add_new_developer(storage, 2, 'Johny',
                  'Silverhand',2, 1.5,
                  age=27, department='DevOps')

add_new_developer(storage, 3, 'Panam',
                  'Palmer',5, 170.5, 'UAH',
                  projects=['Project1', 'Project2', 'Project3'])

add_new_developer(storage, 4, 'Jackie',
                  'Welles',3, 2.7, 'EUR')

print(f'storage: {storage}')

#Task 2

def get_developer_by_id(storage:list, id: int) -> dict:
    found = {}
    for item in storage:
        if item['id'] == id:
            found = item
            break
    return found

get_developer_by_id(storage, 1)
get_developer_by_id(storage, 3)

# Task 3

def update_developer_by_id(storage:list, dev_id:int, **kwargs) -> None:
    found_dev = get_developer_by_id(storage, dev_id)
    new_id = kwargs.get('id')

    if any(item.get('id') == new_id for item in storage):
        print('Developer with specified id already exist')
        pass
    else:
        found_dev.update(kwargs)
        print('updated storage: ', storage)

    if 'work_experience' in found_dev:
        found_dev['work experience'] = found_dev.pop('work_experience')

update_developer_by_id(storage, 1, id=2)
update_developer_by_id(storage, 4, work_experience=4, currency='USD', age=24)

# Task 4
def remove_developer_by_id(storage:list, id:int) -> None:
    found_dev = get_developer_by_id(storage, id)

    if found_dev:
        storage.remove(found_dev)
    else:
        pass

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

storage = sorted(storage, key=lambda dev: dev['work experience'])
print(f'storage: {storage}')

experienced_devs = list(filter(lambda dev: dev['work experience'] > 3, storage))
print(f'storage Exp: {experienced_devs}')

usd_to_uah = 41.47

converted_storage = list(map(
    lambda dev: {
    **dev,
    'salary_uah': round(dev['salary'] * usd_to_uah, 2)
    }, storage
))
print(f'converted_storage: {converted_storage}')
