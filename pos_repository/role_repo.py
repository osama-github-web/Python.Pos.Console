from pos_logic.roles.role import getAllRoles, createTable as createRolesTable, addRole, updateRole, deleteRole, getRole


#region role functions
def role_menu():
    print('01: Add Role')
    print('02: Update Role')
    print('03: Get Role By ID')
    print('04: Get All Role')
    print('05: Delete Role By ID')

def role_operations():
    role_input = int(input('Enter your choice: '))       
    if role_input == 1:
        role_name = input('Enter Name of Role: ')
        addRole(role_name)
    elif role_input == 2:
        role_name = input('Enter Name of Role: ')
        role_id = int(input('Enter Role ID: '))
        updateRole(role_id, role_name)
    elif role_input == 3:
        role_id = int(input('Enter id: '))
        getRole(role_id)
    elif role_input == 4:
        roles = getAllRoles()
        for role in roles:
            print(role[0:])
    elif role_input == 5:
        role_id = int(input('Enter Role ID: '))
        deleteRole(role_id) 
#endregion
