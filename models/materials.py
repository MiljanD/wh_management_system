import time
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta




def manually_adding(con):
    """
    Manual addition of materials to stock
    :param con: database connection
    :return: name of action, code of action which will be used as parameters for add_action function
    """
    cursor = con.cursor()
    material_name = input("Enter material name: ").upper()
    batch = input("Enter batch of material: ")
    usable_for = int(input("Usable for(in years): "))
    quantity = int(input("Quantity: "))
    position = input("Place it on position: ").upper()

    date_of_receipt = datetime.now()
    date_of_expiry = date_of_receipt + relativedelta(years=usable_for)


    query = ("INSERT INTO materials (mat_name, batch, date_of_receipt, expiration_date, quantity, position)"
             "VALUES (%s, %s, %s, %s, %s, %s)")
    cursor.execute(query, (material_name, batch, date_of_receipt, date_of_expiry, quantity, position))
    con.commit()
    cursor.close()

    print(f"On position {position} is added {material_name} in quantity of {quantity} pieces.")
    time.sleep(1.5)
    os.system("cls")
    return {"action": "manual addition", "action_code": 101}


def show_material_by(con, column_name, criterion):
    """
    displays materials by certain criterion
    :param con: database connection
    :param column_name: column name from materials database table
    :param criterion: material name, batch, ... etc.

    """
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM materials WHERE {column_name} = %s", criterion)
    result = cursor.fetchall()

    cursor.close()
    return result


def edit_material_record(con, mat_id, column_name, new_value):
    """
    responsible for editing existing materials in database
    :param con: database connection
    :param mat_id: material id
    :param column_name: name of the column from materials table
    :param new_value: new value that will be entered in materials table

    """
    cursor = con.cursor()
    if column_name == "quantity":
       new_value = int(new_value)
    elif column_name == "mat_name" or column_name == "position":
        new_value = new_value.upper()

    cursor.execute(f"UPDATE materials SET {column_name} = %s WHERE id = %s", (new_value, mat_id))
    con.commit()
    cursor.close()


def show_mat_by_exp_date(con, mat_name):
    """
    responsible for extracting list of materials from db table sorted by expiration date
    :param con: db connection
    :param mat_name: material name
    :return: sorted data from db
    """
    cursor = con.cursor()

    cursor.execute("SELECT * FROM materials WHERE mat_name = %s ORDER BY expiration_date", mat_name)
    con.commit()
    result = cursor.fetchall()
    cursor.close()

    return result


def issue_material(con, mat_id, qty_to_issue, qty_on_stock):
    """
    handles issuing materials to production
    :param con: db connection
    :param mat_id: material ID
    :param qty_to_issue: how much pcs is need to be issued
    :param qty_on_stock: available qty on stock
    :return: action name and action code
    """
    cursor = con.cursor()
    new_qty = qty_on_stock - qty_to_issue
    cursor.execute("UPDATE materials SET quantity = %s WHERE id = %s", (new_qty, mat_id))
    con.commit()
    cursor.close()

    return {"action": "issue to production", "action_code": 201}


def return_on_stock(con, mat_id, new_qty):
    """
    handles return of unused qty of materials back to stock
    if there is certain batch of certain material on stock in wh
    :param con: db connection
    :param mat_id: material ID
    :param new_qty: quantity to return
    :return: action name and action code
    """
    cursor = con.cursor()
    cursor.execute("UPDATE materials SET quantity = %s WHERE id = %s", (new_qty, mat_id))
    con.commit()
    cursor.close()

    return {"action": "return on stock", "action_code": 301}


