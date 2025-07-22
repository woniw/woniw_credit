from data.json_management import save_json
from data.variables import data
from data.variables import green
from data.variables import red
import logging

def clear_current_login():
    try:
        data['current_login']['username'] = ""
        data['current_login']['password'] = ""

        save_json("data.json", data)
        print(f"{green} TEMPORARY LOGIN HAS BEEN SUCCESSFULLY CLEARED!")
    except:
        logging.critical(f"{red} SOMETHING WENT WRONG WITH THE TEMPORARY LOGIN CLEARING FUNCTION")