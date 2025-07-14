from models.db import connection
from models.users import register, login

user_info = ["novi", "dm3004)_", "miljan", "duvnjak", "admin"]

# register(connection, user_info[0], user_info[1], user_info[2], user_info[3], user_info[4])

login(connection, "novi", "dm3004)_")