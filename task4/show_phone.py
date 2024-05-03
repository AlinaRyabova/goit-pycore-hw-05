from input_error import input_error

@input_error
def show_phone(args, contacts):
    if len(args) == 2 and args[0] == "phone":
        name = args[1]
        phone = contacts.get(name, None)
        if phone is None:
            return KeyError
        return f"{name}: {phone}"
 


