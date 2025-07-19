# from db import connection

def add_action(con, action, action_code, user_id):
    cursor = con.cursor()

    query = ("INSERT INTO actions (action, action_code, user)"
             "VALUES (%s, %s, %s)")

    cursor.execute(query, (action, action_code, user_id))
    con.commit()
    cursor.close()

#
# def show_user(con, user_id):
#
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM actions WHERE id = %s", user_id)
#     con.commit()
#
#     action = cursor.fetchone()
#
#     new_cursor = con.cursor()
#     new_cursor.execute("SELECT * FROM users WHERE id = %s", action["id"])
#     con.commit()
#     username = new_cursor.fetchone()
#     print(username)
#
#     cursor.close()
#     new_cursor.close()
#
#
# show_user(connection, 1)