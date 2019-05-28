from config import Config
from flask import Flask
from flask_pymongo import PyMongo


#db = PyMongo()

def create_app():
    app = Flask(__name__)

    #app.config.from_object((get_environment_config()))
    #db.init_app(app)

    #@app.before_first_request
    #def initialize_database():
    #    """ Create all tables """
    #    db.create_all()

    #@app.teardown_appcontext
    #def shutdown_session(exception=None):
    #    db.session.remove()

    @app.route("/")
    def hello_world():
        return "Rosie je t'aime !!!!!"

    return app

#def get_environment_config():
#    if Config.ENV == "PRODUCTION":
#        return "config.ProductionConfig"
#    elif Config.ENV == "DEVELOPMENT":
#        return "config.DevelopmentConfig"