from flask import redirect, render_template, request

from gdtot import app
from gdtot.generator import get_links


@app.route("/direct")
def direct_page():
    link = request.args.get("url")
    if link:
        try:
            drive_link, direct_link, _ = get_links(link=link, cookies=request.cookies)
        except ValueError as err:
            return render_template("error.html", error=str(err)), 400
        return redirect(direct_link)
    return render_template("404.html"), 404
