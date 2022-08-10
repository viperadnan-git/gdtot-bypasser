import json
import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

if os.path.exists("cookies.json"):
    with open("cookies.json") as f:
        default_cookies = json.load(f)
else:
    default_cookies = [
        {"PHPSESSID": os.environ["PHPSESSID"], "crypt": os.environ["CRYPT"]}
    ]

gdown_base_url = os.environ("GDOWN_URL", "https://gdown.arnid.workers.dev/download?id=")

app = Flask(__name__, static_folder="static", static_url_path="/static")

from .routes import direct_link, drive_link, home, link, set_cookie
