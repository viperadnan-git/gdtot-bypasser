import json, os
from decouple import config
from flask import Flask


try:
    gdown_base_url = config("GDOWN_URL", default="https://gdown.arnid.workers.dev/download?id=")
    php_sess_id = config("PHPSESSID")
    crypt = config("CRYPT")
except Exception as err:
    print(err)
    print("PHPSESSID & CRYPT Not Found!")
    exit()

if os.path.exists("cookies.json"):
    with open("cookies.json") as f:
        default_cookies = json.load(f)
else:
    default_cookies = [
        {"PHPSESSID": php_sess_id, "crypt": crypt}
    ]


app = Flask(__name__, static_folder="static", static_url_path="/static")

from .routes import direct_link, drive_link, home, link, set_cookie
