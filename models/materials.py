import time
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Tasks: ADD MATERIALS: 1. add from inv., ISSUE OR RETURN: 201 and 203, CORRECTIONS:

def manually_adding(con):
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


def add_from_invoice():
    pass


def show_material_by(con, column_name, criterion):
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM materials WHERE {column_name} = %s", criterion)
    result = cursor.fetchall()

    cursor.close()
    return result


def edit_material_record(con, mat_id, column_name, new_value):
    cursor = con.cursor()
    if column_name == "quantity":
       new_value = int(new_value)
    elif column_name == "mat_name" or column_name == "position":
        new_value = new_value.upper()

    cursor.execute(f"UPDATE materials SET {column_name} = %s WHERE id = %s", (new_value, mat_id))
    con.commit()
    cursor.close()


def show_mat_by_exp_date(con, mat_name):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM materials WHERE mat_name = %s ORDER BY expiration_date", mat_name)
    con.commit()
    result = cursor.fetchall()
    cursor.close()

    return result


def issue_material(con, mat_id, qty_to_issue, qty_on_stock):
    cursor = con.cursor()
    new_qty = qty_on_stock - qty_to_issue
    cursor.execute("UPDATE materials SET quantity = %s WHERE id = %s", (new_qty, mat_id))
    con.commit()
    cursor.close()

    return {"action": "issue to production", "action_code": 201}


def return_on_stock(con, mat_id, new_qty):
    cursor = con.cursor()
    cursor.execute("UPDATE materials SET quantity = %s WHERE id = %s", (new_qty, mat_id))
    con.commit()
    cursor.close()

    return {"action": "return on stock", "action_code": 301}


