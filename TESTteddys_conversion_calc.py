# Dear user,
# My name is Teddy and I made this program as a class project to help you convert numbers!
# Thank you for using my code :)

def intro(): #intro message for the user
    print("")
    print("Welcome to Teddy's Conversion Calculator :) ")
    print("")
    print("This program can convert numbers!")
    print("")

def menu(): #used to display the menu for conversion options
    conv_opt = {
        'D' : 'Decimal to Binary',
        'B' : 'Binary to Decimal'

        }
    return conv_opt

def display_menu(conv_opt): # gives the user the choice of conversion method
    print("How would you like to convert your numbers?")
    for items, values in conv_opt.items():
        print(items+ ". "+ values.replace('_', ' ').capitalize())
    menu_selection = input("Type D for Decimal to Binary, OR type B for Binary to Decimal: ").upper()
    print("")
    #confirm user selection
    print("You chose to convert using {}! I'll be happy to help <3".format(conv_opt[menu_selection]))


def another_stop(): #gives the user an option to convert more numbers or stop the program
    print("Thank you for using my calculater!")
    answer = input("Would you like to convert another number?")
    conv_opt = {
        'Y' : 'Yes please!',
        'N' : 'No, thank you.'
        }
    return yes_no
    while answer != 'Y':
         print("This program will now end. Goodbye! :) ")
    while answer == 'Y':
        return display_menu

def main():

    intro()

    menu_selection = 'D'
    items_list = []
    while menu_selection in ['D', 'B']:
        conv_opt = menu()
        menu_selection = display_menu(conv_opt)


    another_stop()
    print("This program will end now. Goodbye! :) ")

if __name__ == "__main__":
    main()
