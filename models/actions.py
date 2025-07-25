from pathlib import Path
from datetime import datetime
from models.users import show_users

def add_action(con, action, action_code, user_id):
    cursor = con.cursor()
    current_date = datetime.now()
    query = ("INSERT INTO actions (action, action_code, user, date)"
             "VALUES (%s, %s, %s, %s)")

    cursor.execute(query, (action, action_code, user_id, current_date))
    con.commit()
    cursor.close()


def generate_report(con, project_path):
    dir_name = "reports"
    report_name = f"report_{datetime.now().strftime('%d-%m-%Y')}.txt"
    report_path = Path(project_path)/dir_name/report_name
    current_date = datetime.now().date()

    cursor = con.cursor()
    cursor.execute("SELECT * FROM actions WHERE date = %s", current_date)
    con.commit()
    results = cursor.fetchall()
    cursor.close()

    if results:
        action_summary = {"actions": {}, "users": {}}
        list_of_actions = []
        users_infos = []
        for result in results:
            if result["user"] not in users_infos:
                action_summary["users"][result["user"]] = 1
                users_infos.append(result["user"])
            else:
                action_summary["users"][result["user"]] = action_summary["users"][result["user"]] + 1

            if result["action"] in list_of_actions:

                action_summary["actions"][result["action"]] = action_summary["actions"][result["action"]] + 1
            else:
                action_summary["actions"][result["action"]] = 1
                list_of_actions.append(result["action"])

        with open(f"{report_path}", "w") as file:
            file.write(f"Report for date {current_date}\n\n")
            file.write("Action section:\n")
            content = ""
            user_content = ""
            for key, action in action_summary.items():
                if key == "actions":
                    for act_key, act in action.items():
                        content += f"Action {act_key.upper()} is done: {act} times.\n"

                elif key == "users":
                    for user_key, user_act_count in action.items():
                        user_data = show_users(con)
                        for user in user_data:
                            if user["id"] == user_key:
                                user_content += (f"User {user["name"].capitalize()} {user["surname"].capitalize()} "
                                                 f"has done {user_act_count} actions.\n")

            file.write(content)
            file.write("\nUser section:\n")
            file.write(user_content)

    else:
        print(f"There is no actions for date {current_date}.")


