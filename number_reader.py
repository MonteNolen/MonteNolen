import json

try:
    filename = 'numbers.json'
    with open(filename, 'r') as f_obj:
        numbers = json.load(f_obj)
except:
    print('нет такого файла')
else:
    print(numbers)