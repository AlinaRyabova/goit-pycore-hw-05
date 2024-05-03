from input_error import input_error

@input_error
def add_contact(args, contacts):
    if len(args) == 0:
        name = input("Enter the name for the contact: ")
        phone = input("Enter the phone number for the contact: ")
    elif len(args) == 1:
        name = args[0]
        phone = input("Enter the phone number for the contact: ")
    elif len(args) == 2:
        name, phone = args
    else:
        raise ValueError

    contacts[name] = phone
    return "Contact added."