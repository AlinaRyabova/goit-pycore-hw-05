from input_error import input_error

@input_error
def show_all(args, contacts):
    if len(args) != 0:
        return "Invalid command or arguments."
    if not contacts:
        return "No contacts saved."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        