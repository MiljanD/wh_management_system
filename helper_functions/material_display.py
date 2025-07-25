from datetime import date


def show_materials(material_list, return_on_stock=False):
    """
    way of displaying available materials
    :param material_list: list of available materials
    :param return_on_stock: by default is False and able printing of material list
    :return: just printing desired outcome
    """
    col_names = []
    for mat in material_list:
        col_names = [key for key, value in mat.items()]
        print(
            f"\nOn position {mat["position"].upper()} is placed {mat["quantity"]} pieces of {mat["mat_name"]} material with batch {mat["batch"]}")
        print(f"Material ID is {mat["id"]}")
        print(f"Expiration date of this batch: {mat["expiration_date"]}")

    if not return_on_stock:
        col_names_list = ""
        for idx, name in enumerate(col_names[1:]):
            col_names_list += f"{idx + 1}. {name}{' ' * 2}"
        print("\nColumn names:")
        print(col_names_list)


def collect_data_edit():
    """
    edit form for correction of already entered data
    :return: edit data
    """
    mat_id = int(input("\nChose material ID: "))
    column_criterion = input("Chose column for edit: ")
    if column_criterion == "date_of_receipt" or column_criterion == "expiration_date":
        date_value = input("Enter dates in form of YYYY-MM-DD: ")
        date_list = date_value.split("-")

        new_value = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))

    else:
        new_value = input(f"Enter new value for column {column_criterion}: ")

    return {"mat_id": mat_id, "col_name": column_criterion, "new_value": new_value}


def materials_by_exp(material_list):
    """
    displays materials sorted by expiration date
    :param material_list: sorted material list
    :return: just printing desired outcome
    """
    for idx, mat in enumerate(material_list):
        print(f"Material ID: {mat["id"]}")
        print(f"Position of material: {mat["position"]}")
        print(f"Material info: {mat["mat_name"]} {mat["expiration_date"]} {mat["quantity"]}\n")


