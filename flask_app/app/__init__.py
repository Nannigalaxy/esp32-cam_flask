from flask import Flask

app = Flask(__name__)
# app.config['DEBUG'] = True
app.secret_key = 'sdfhj43uop23opjuhjg234jghds8'
app.jinja_env.globals.update(zip=zip)
from app import routes