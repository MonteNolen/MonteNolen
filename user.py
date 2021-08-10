class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("\tИмя: %s" %self.first_name.title())
        print("\tФамилия: %s" %self.last_name.title())
        print("\tВозраст: %s лет" %self.age)
    def greet_user(self):
        print("\nЗдравствуй, %s." %self.first_name.title())
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

new_user = User('иван', 'петров', 20)
new_user.describe_user()
new_user.greet_user()
print(new_user.login_attempts)
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempts()
print(new_user.login_attempts)