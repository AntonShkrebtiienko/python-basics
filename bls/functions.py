# Task 1
storage: list = []

def add_new_developer(storage: list, id: int,
                      first_name: str, last_name:str,
                      work_experience: int, salary:float,
                      currency: str = 'USD', **kwargs):

    data: dict = locals()
    developer: dict = {k: v for k, v in data.items() if k != "storage"}
    developer_cleaned: dict = {k: v for k, v in developer.items() if k != "kwargs"}

    match developer:

        case {'kwargs': item} if item:
            developer_cleaned.update(item)
            storage.append(developer_cleaned)

        case {'kwargs': {}}:
            storage.append(developer_cleaned)


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

def get_developer_by_id(storage:list, id: int):

    for item in storage:
        match item:
            case {'id': i} if i == id:
                print(item)
                return item
    return None

get_developer_by_id(storage, 1)
get_developer_by_id(storage, 3)

# Task 3

def update_developer_by_id(storage:list, dev_id:int, **kwargs):
    found_id = any(dev['id'] == kwargs.get('id') for dev in storage)

    for item in storage:
        match item:
            case {'id': i} if i == dev_id and found_id:
                print('Developer with specified id already exist')
                pass
            case {'id': i} if i == dev_id and not found_id :
                item.update(kwargs)
                print(f'storage: {storage}')
            case _:
                pass

update_developer_by_id(storage, 1, id=2)
update_developer_by_id(storage, 4, work_experience=4, currency='USD', age=24)

# Task 4
def remove_developer_by_id(storage:list, id:int):

    for item in storage:
        match item:
            case {'id': i} if i == id:
                storage.remove(item)
                print(f'storage: {storage}')
                break
            case _:
                pass

remove_developer_by_id(storage, 3)

# Task 5
def add_projects(developer: dict, *args):

    if 'projects' not in developer:
        developer['projects'] = list(args[0])
    elif isinstance(developer['projects'], list):
        developer['projects'].extend(args[0])
    else:
        print('Developer already has "projects" key and its not a list type')

add_projects(storage[0], ['Smart House', 'Stream Platform',
                                'Audio Translator', 'Tron', 'LOL'] )
add_projects(storage[0], ['Smart House', 'Stream Platform',
                                'Audio Translator', 'Tron', 'LOL'] )

# Task 6

storage = sorted(storage, key=lambda dev: dev['work_experience'])
print(f'storage: {storage}')

experienced_devs = list(filter(lambda dev: dev['work_experience'] > 3, storage))
print(f'storage Exp: {experienced_devs}')

usd_to_uah = 41.47

converted_storage = list(map(lambda dev: {
    **dev,
    'salary_uah': round(dev['salary'] * usd_to_uah, 2)
}, storage))
print(f'converted_storage: {converted_storage}')