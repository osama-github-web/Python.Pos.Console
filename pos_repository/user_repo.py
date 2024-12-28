from pos_logic.users.user import getAllUsers,createTable as createUsersTable, addUser, updateUser,deleteUser, getUser, addRoleToUser
from pos_logic.roles.role import getAllRoles


#region user functions
def user_menu():
    print('01: Add User')
    print('02: Update User By Name')
    print('03: Get User By ID')
    print('04: Get All User')
    print('05: Delete User By ID')
    print('06: Assign Role to User')

def user_operations():
    user_input = int(input('Enter your choice: '))
    if user_input == 1:
        name = input('Enter Name of User: ')
        email = input('Enter Email of User: ')
        phone = input('Enter Phone of User: ')
        addUser(name, email, phone)
    elif user_input == 2:
        name = input('Enter Name of User: ')
        email = input('Enter Email of User: ')
        phone = input('Enter Phone of User: ')
        updateUser(name, email, phone)
    elif user_input == 3:
        user_id = int(input('Enter User ID: '))
        getUser(user_id)
    elif user_input == 4:
        users= getAllUsers()
        for user in users:        
            print(str(user[0:]))
    elif user_input == 5:
        user_id = int(input('Enter User ID: '))
        deleteUser(user_id)
    elif user_input == 6:
        all_roles = getAllRoles()
        all_users = getAllUsers()
        for role in all_roles:
            print(str(role[0:]))
        for user in all_users:
            print(str(user[0:]))
        user_id = int(input('Enter User ID: '))
        role_id = int(input('Enter Role ID: '))
        addRoleToUser(user_id, role_id)
#endregion
