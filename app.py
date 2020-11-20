from logging import debug
from App.Blueprints.Dashboard import gameRoom
from flask import Flask

from App.Database import db
from App.Blueprints.Landing import landing
from App.Blueprints.Dashboard import dashboard
from App.Blueprints.Dashboard import learningenv
from App.Blueprints.Dashboard import gameRoom
from App.LoginManager import login_manager
from App.Blueprints.Administrator import admin
from App.Websockets.base import websockets
from App.Tests.database import populate_database
from config import BasicConfig


app = Flask(__name__)

app.config.from_object(BasicConfig)

db.init_app(app)

login_manager.init_app(app)

app.register_blueprint(landing)
app.register_blueprint(dashboard)
app.register_blueprint(learningenv)
app.register_blueprint(gameRoom)


admin.init_app(app)


with app.app_context():
    db.create_all()
    populate_database()

websockets.init_app(app)

websockets.run(app, log_output=True, debug=True, port=5000)
