import os
from dotenv import load_dotenv


def load_credentials():
    load_dotenv()
    username = os.environ.get("CARA_USERNAME")
    password = os.environ.get("CARA_PASSWORD")
    return username, password
