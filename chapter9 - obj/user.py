class User(object):
    def __init__(self, name):
        self.name = name
        self.login_attempts = 0
    def login(self):
        self.increment_login_attempts()
        print("You have logged in " + str(self.login_attempts) + " times.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    
a = User("X")
a.login()
a.login()
a.reset_login_attempts()
a.login()

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.privileges = Privileges()
    

class Privileges(object):
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print("Privileges: ")
        for privilege in self.privileges:
            print(privilege)

admin = Admin("X")
admin.privileges.show_privileges()
        