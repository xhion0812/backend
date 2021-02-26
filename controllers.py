from flask.views import MethodView
from flask import jsonify, request
import time



class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        if (email == "test@gmail.com" and password == "12345"):
            return jsonify({"auth": True, "name": "Pepe Perez", "token": token}), 200
        return jsonify({"auth": False}), 401

class RegistroUserControllers(MethodView):

    def post(self):
    
        time.sleep(3)
        content = request.get_json()
        nombres = content.get("nombres")
        apellidos = content.get("apellidos")
        cedula = content.get("cedula")
        direccion = content.get("direccion")
        telefono = content.get("telefono")
        correo = content.get("correo")
        password = content.get("password")
        password_verifi = content.get("password_verifi")

        return jsonify({"login ok": True, "nombres": nombres, "apellidos": apellidos, "cedula": cedula, "direccion": direccion, "telefono": telefono, "correo": correo}), 200
    


class InicioSesionUserControllers(MethodView):

    def post(self):
        time.sleep(3)
        content = request.get_json()
        nombre = content.get("nombre")
        password = content.get("password")
        return jsonify({"login ok": True, "nombre": nombre}), 200

class InicioUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasGranosUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasCarnesUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasVerdurasUserControllers(MethodView):
    
    def post(self):
       pass