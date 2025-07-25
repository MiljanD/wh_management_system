import pymysql

# establishing connection to the project database

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="dm3004^mk2606",
    database="wh_management",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("Database connected.")
else:
    print("Connection to database failed.")