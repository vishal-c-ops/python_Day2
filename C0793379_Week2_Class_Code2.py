print("___________________________Program to print fullname in reverse order--------------------------------")


def get_input():
    global f_name, l_name
    f_name = input("Enter your first name:")
    l_name = input("Enter your last name:")


def display_name():
    print("The full name of user is :" + l_name + " " + f_name)


def main():
    get_input()
    display_name()


main()
