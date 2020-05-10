# def handle_error_1(func):
#     def wrapper(*args):
#         try:
#             return func(*args)
#         except TypeError:
#             print('No username defined!')
#     return wrapper

def handle_error_2(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            raise TypeError("Данные введены не верно")
        else:
            print("Everything is okay")
        finally:
            print("End")
    return wrapper


# @handle_error_1
@handle_error_2
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_account_balance(self):
        if bool(self.username) == True:
            return self.username

    def change_password(self):
        if bool(self.password) == True:
            return self.password
    
u = User("Beken", 123)
print(u.get_account_balance())
print(u.change_password())
