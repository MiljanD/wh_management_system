

def display_user_list(list_of_users):
    """
    displays list of all registered users
    :param list_of_users: list of users
    :return: dictionary of columns and values
    """
    column_names = []
    for idx, user in enumerate(list_of_users):
        column_names = [key for key, value in user.items()]
        list_line = f"\n{idx + 1}. User ID: {user["id"]} User full name: {user["name"].capitalize()} {user["surname"].capitalize()} User role: {user["role"]}"
        print(list_line)
        print("-" * len(list_line))

    column_list = ""
    for idx, column in enumerate(column_names[1:]):
        column_list += f"{idx + 1}. Column name: {column}{' ' * 2}"

    return {"list": column_list, "col_names": column_names}