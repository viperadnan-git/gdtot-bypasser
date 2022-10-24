from decouple import config

from gdtot import app

app.run(
    host=config("HOST", default="0.0.0.0"),
    port=config("PORT", default=8000),
    debug=config("DEBUG", default=False, cast=bool),
)
