from flask_script import Server, Manager
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from app.main import create_app

app = create_app()
manager = Manager(app)
manager.add_command("runserver", Server)

#mongo = PyMongo(app)


if __name__ == "__main__":
    manager.run()