class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' ' + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' Open')
    def print_numbers(self):
        print('Количество посетителей' + ' ' + self.number_served)
    def set_number_served(self, num):
        self.number_served = num
    def increment_number_served(self, num):
        if num > 0:
            self.number_served += num
        else:
            print('Нельзя добавить "0" или меньше нуля.')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['red', 'blue', 'white']
    def out_isecream(self):
        for i in self.flavors:
            print(i.title(), end=' ')
my_cream = IceCreamStand('morojenoe', 'ice')
my_cream.out_isecream()

    