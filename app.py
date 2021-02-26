from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])

app.add_url_rule(user["registro_user"], view_func=user["registro_user_controllers"])
app.add_url_rule(user["inicio-sesion_user"], view_func=user["inicio-sesion_user_controllers"])

app.add_url_rule(user["inicio_user"], view_func=user["inicio_user_controllers"])
app.add_url_rule(user["categoriasgranos_user"], view_func=user["categoriasgranos_user_controllers"])
app.add_url_rule(user["categoriascarnes_user"], view_func=user["categoriascarnes_user_controllers"])
app.add_url_rule(user["categoriasverduras_user"], view_func=user["categoriasverduras_user_controllers"])