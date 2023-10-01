from flask import Flask, render_template
from dotenv import dotenv_values
ENV = dotenv_values()


def create_app():
    app = Flask(__name__)

    # CONFIG
    app.config["SECRET_KEY"] = ENV['SECRET_KEY']

    # BLUEPRINT
    from .views.landing import landing

    app.register_blueprint(landing, url_prefix="/")
    
    return app

