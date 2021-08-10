#словари

people = {
    'user': {
        'first': 'enrico',
        'last': 'fermi',
        'age': ['99'],
        'city': 'Gotem'
            },
    'user2': {
        'first': 'йцукен',
        'last': '1234',
        'age': ['11', '12', '123'],
        'city': 'Яфцук'
            }
}
people['user3'] = {'first': 'asdasdad',
        'last': 'asdasdasdasdasda',
        'age': ['123'],
        'city': 'Яфцук'}
        
for key, value in people.items():   
    print(key)
    fulname = value['first'] + " " + value['last']
    location = value['city']
    print("\tFulname: " + fulname.title())
    print("\tLocation: " + location.title())
    for age in value['age']:
        print("\tAge: " + age)
    
