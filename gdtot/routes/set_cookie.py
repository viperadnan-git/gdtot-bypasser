from http.cookies import SimpleCookie

from flask import make_response, redirect, request

from gdtot import app


@app.route("/setcookie/<path:rawdata>")
def setcookie_page(rawdata):
    cookie = SimpleCookie()
    cookie.load(rawdata)

    resp = make_response(redirect("/"))
    for key, value in cookie.items():
        resp.set_cookie(key=key, value=value.value, expires=3650)

    return resp
