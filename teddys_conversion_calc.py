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
    return menu_selection.upper()


def check_bin_number(numbers):
    for number in numbers:
        if number not in ['0', '1']:
            return (True, None)
    return (False, numbers)

def bin_to_dec(number):
     result = 0
     if len(number) > 0:
       power = len(str(number)) - 1 #determine greatest power
       for num in str(number):
           result += int(num) * 2 ** power
           power -= 1 #decrease by 1
       return result

def check_dec_number(number):
    try:
        return (False, int(number))
    except:
        print("invalid input: please use whole numbers!")
        return (True, None)

def dec_to_bin(number):
    result = ""
    number = int(number)
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result  #place string in reverse order
    return result

def another_stop(yes_no): #gives the user an option to convert more numbers or stop the program
    print("Thank you for using my calculater!")
    if answer == 'Y':
        display_menu()
    if answer == 'N':
         print("This program will now end. Goodbye! :) ")

def main():
#intro message for user
    intro()
#menu
    menu_selection = '#'
    items_list = []
    while menu_selection not in ['D', 'B']:
        conv_opt = menu()
        menu_selection = display_menu(conv_opt)

#check for valid number and convert numbers
    make_selection = True
    while make_selection:
        if menu_selection == 'D':
            selection = input("Type your decimal number here: ")
            make_selection, selection = check_dec_number(selection)
            dec_to_bin(selection)
            print("Decimal {} to Binary: {}".format(selection, dec_to_bin(selection)))
        elif menu_selection == 'B':
            selection = input("Type your binary number here: ")
            make_selection, selection = check_bin_number(selection)
            bin_to_dec(selection)
            print("Binary to Decimal: {}".format(bin_to_dec(selection)))
        else:
            print("nothing here")
            make_selection = False
#outro


if __name__ == "__main__":
    main()
