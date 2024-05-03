def parse_input(user_input):
    # Розділити введений рядок за комами, а не за пробілами
    cmd, *args = user_input.split(', ')
    # Перевести команду в нижній регістр і видалити зайві пробіли
    cmd = cmd.strip().lower()
    # Повернути кортеж з командою та її аргументами
    return cmd, args