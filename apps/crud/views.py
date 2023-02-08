from flask import Blueprint

crud = Blueprint("crud", __name__, template_folder="templates", static_folder="static")


@crud.route("/")
def index():
    return "Hello from Flask!"
