from pos_repository.user_repo import user_menu, user_operations
from pos_repository.product_repo import product_menu, product_operations
from pos_repository.role_repo import role_menu, role_operations

def user_choice(input):
    if input == 1:
        user_menu()
        user_operations()
              
    elif input == 2:
        role_menu()
        role_operations()

    elif input == 3:
        product_menu()
        product_operations()

    else:
        print('Invalid option')

#region main menu
def main_menu():
    print('01: Print User Menu')
    print('02: Print Role Menu')
    print('03: Print Product Menu')
    input_choice = int(input("Enter your choice (1,2,3): "))
    user_choice(input_choice)
#endregion
