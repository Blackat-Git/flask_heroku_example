import os
from flask import Flask, render_template

app = Flask('MyHerokuApp')

# Read the mailgun secret key from environment variables

# This is needed for Heroku configuration, as in Heroku our
# app will probably not run on port 5000, as Heroku will automatically
# assign a port for our application
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():

    # We will just display our mailgun secret key, nothing more.
    return "333"

# Route that will get the config value based on a provided key, so in
# this way we can interogate our configuration.
@app.route('/<config_key>')
def key(config_key=None):
    config_value=None
    return "333"


app.run(host='0.0.0.0', port=port, debug=True)
