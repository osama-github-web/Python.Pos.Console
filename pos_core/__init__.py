from pos_core.pos_main_menu import main_menu

#region Initialization/Starting Point
def __init__():
    # Initialize a variable
    isTrue = True

    # Simulating a do while loop
    while isTrue:
        main_menu()
        print('01: Press 1 if you want to Proceed: ')
        print('02: Press 2 to Exit: ')
        enter_choice = int(input('Enter your choice(1,2): '))

        if enter_choice == 2:
            print("Exiting Program")
            break
#endregion