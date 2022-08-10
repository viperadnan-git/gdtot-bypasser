import random
import re
import urllib.parse as urlparse
from urllib.parse import parse_qs

import requests
from bs4 import BeautifulSoup

from gdtot import default_cookies, gdown_base_url


def GDTOT(url: str, cookies: dict) -> str:
    """Gdtot google drive link generator
    By https://github.com/oxosec"""

    headers = {
        "upgrade-insecure-requests": "1",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A Dual) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "document",
        "referer": "",
        "prefetchAd_3621940": "true",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    r1 = requests.get(
        url, headers=headers, cookies=cookies, allow_redirects=True
    ).content
    s1 = (
        BeautifulSoup(r1, "html.parser")
        .find("button", id="down")
        .get("onclick")
        .split("'")[1]
    )
    headers["referer"] = url
    s2 = (
        BeautifulSoup(
            requests.get(
                s1, headers=headers, cookies=cookies, allow_redirects=True
            ).content,
            "html.parser",
        )
        .find("meta")
        .get("content")
        .split("=", 1)[1]
    )
    headers["referer"] = s1
    s3 = BeautifulSoup(
        requests.get(
            s2, headers=headers, cookies=cookies, allow_redirects=True
        ).content,
        "html.parser",
    ).find("div", align="center")
    if s3 is None:
        s3 = BeautifulSoup(
            requests.get(
                s2, headers=headers, cookies=cookies, allow_redirects=True
            ).content,
            "html.parser",
        )
        status = s3.find("h4").text
        raise ValueError(status)
    else:
        gdlink = s3.find(
            "a", class_="btn btn-outline-light btn-user font-weight-bold"
        ).get("href")
        filename = s3.find(
            "h6", class_="m-0 font-weight-bold text-light"
        ).string.replace("Download ", "")
        return gdlink, filename


def getIdFromUrl(link: str):
    if "folders" in link or "file" in link:
        regex = r"https://drive\.google\.com/(drive)?/?u?/?\d?/?(mobile)?/?(file)?(folders)?/?d?/([-\w]+)[?+]?/?(w+)?"
        res = re.search(regex, link)
        if res is None:
            raise IndexError("GDrive ID not found.")
        return res.group(5)
    parsed = urlparse.urlparse(link)
    return parse_qs(parsed.query)["id"][0]


def get_links(link, cookies):
    if not cookies.get("crypt") or not cookies.get("PHPSESSID"):
        cookies = random.choice(default_cookies)
    else:
        cookies = {"PHPSESSID": cookies.get("PHPSESSID"), "crypt": cookies.get("crypt")}
    try:
        drive_link, filename = GDTOT(link, cookies=cookies)
    except Exception as err:
        raise ValueError(str(err))
    direct_link = gdown_base_url + getIdFromUrl(drive_link)
    return drive_link, direct_link, filename
