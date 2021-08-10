import json

def get_storage_number():
    filename = 'number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
    else:
        return number

def get_new_number():
    number = input('Введите любимое число: ')
    filename = 'number.json'
    with open(filename, 'w') as f:
        json.dump(number, f, ensure_ascii=False, indent=4, sort_keys = True)
    return number

def print_number():
    number = get_storage_number()
    if number:
        print(f'Твоё любимое число: {number}')
    else:
        number = get_new_number()
        print(f'Я запомнил твоё любимое число: {number}')
print_number()

