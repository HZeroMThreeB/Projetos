import datetime
import logging
import os
import sys

import yaml


CONSUME_FILE = "./config.yml"
GITLAB_USER_LOGIN = os.environ['GITLAB_USER_LOGIN'] = "root"

logging.basicConfig(format='[%(asctime)s] - %(name)s - [%(levelname)s] - %(message)s' ,
                    datefmt='%d/%m/%y %H:%M:%S',
                    level=logging.DEBUG)


#Get config file, made expecting a .yaml
def get_file(config_file: str) -> dict:
    with open(config_file) as file:
        data = yaml.safe_load(file)
    return data


#Unpack get_file() configuration
def unpack_config(data_file: dict ) -> tuple:
    try:
        master_group = data_file["master-user-group"]
        freezing_dates = data_file["freezing-dates"]
    except KeyError:
        logging.error("Check all fields below:\nmaster-user-group, freezing-dates")
        sys.exit(1)
    return master_group, freezing_dates


#return TRUE if USER are in master-user-group. Return FALSE if not.
def is_eval_bypass(bypass_group: dict, user) -> bool:
    return user in bypass_group


def is_bypass_date(date_from, date_to) -> bool:
    today = datetime.date.today()

    return date_from < today <= date_to


def show_config():

    master_users, freezing_dates = unpack_config(get_file(CONSUME_FILE))

    print(f"Freezing date goes from {freezing_dates["from"]} to {freezing_dates['to']}")

    if is_eval_bypass(master_users, GITLAB_USER_LOGIN) and is_bypass_date(freezing_dates["from"], freezing_dates["to"]):
        print(f"Seu usuário \033[32;1m{GITLAB_USER_LOGIN}\033[m tem permissão para quebrar a freezing condition!")

        sys.exit(0)
    else:
        logging.error("Your user are not allowed to break freezing condition or we aren't on freezing condition period.")

        print("Users that are able to breakthrough freezing condition:")
        for user in master_users:
            print(f"{user}")

        sys.exit(1)


if __name__ == "__main__":
    show_config()
