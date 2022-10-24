from flask import render_template, request

from gdtot import app
from gdtot.generator import get_links


@app.route("/link")
def link_page():
    link = request.args.get("url")
    if link:
        try:
            drive_link, direct_link, filename, size = get_links(
                link=link, cookies=request.cookies
            )
        except ValueError as err:
            return render_template("error.html", error=str(err)), 400
        return render_template(
            "link.html",
            drive_link=drive_link,
            direct_link=direct_link,
            filename=f"{filename} {size}",
        )
    return render_template("404.html"), 404
