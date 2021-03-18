from flask.views import MethodView
from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify, request, flash
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
import MySQLdb.cursors
import time
import re

app = Flask(__name__)


app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todito'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
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
        documento = content.get("documento")
        direccion = content.get("direccion")
        telefono = content.get("telefono")
        correo = content.get("correo")
        password = content.get("password")
        password_verifi = content.get("password_verifi")
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO registro (nombres, apellidos, documento, direccion, telefono, correo, pass) VALUES(%s, %s, %s, %s, %s, %s, %s)',(nombres, apellidos, documento, direccion, telefono, correo, password))
        mysql.connection.commit()
        return jsonify({"login ok": True, "nombres": nombres, "apellidos": apellidos, "cedula": documento, "direccion": direccion, "telefono": telefono, "correo": correo}), 200

#@app.route('', methods=['GET', 'POST'])
    #@app.route("/api/v01/user/registro", methods=["POST"])
    """def post(self):
        if request.method == 'POST':
            apellidos = request.form.get()['apellidos']
            nombres = request.form.get()["nombres"]
            documento = request.form.get()["cedula"]
            direccion = request.form.get()["direccion"]
            telefono = request.form.get()["telefono"]
            correo = request.form.get()["correo"]
            contrasena = request.form.get["password"]
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO registro (nombres, apellidos, documento, direccion, telefono, correo, contrasena ) VALUES ('" + 
            str(nombres) + "', '" + 
            str(apellidos) + "', '" + 
            str(documento) + "', '" + 
            str(direccion) + "', '" +
            str(telefono) + "', '" + 
            str(correo) + "', '" + 
            str(contrasena) + "')")
            mysql.connection.commit()
            
            data = {
                "nombres": nombres,
                "apellidos": apellidos,
                "documento": documento,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo,
                "contrasena": contrasena
            }
            print(data)
        return jsonify({"data": data})

"""
class InicioSesionUserControllers(MethodView):

    def post(self):
        time.sleep(3)        
        cursor = mysql.connection.cursor()
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        result = ""

        cursor.execute("SELECT * FROM registro WHERE correo ='" + str(email) + "'")
        rv = cursor.fetchone()

        if bcrypt.check_password_hash(rv['password'], password):
            access_token = create_access_token(identity = {'nombres': rv['nombres'], 'apellidos': rv['apellidos'], 'email': rv['email']})
            result = jsonify({"token":access_token})
        else:
            result = jsonify({"Error":"ivalido el nombre o contraseña"})
        
        return result
        #return jsonify({"login ok": True, "nombre": email}), 200

class TablaControllers(MethodView):
    
    def get(self):
        productos = [{"id": 1, "nombre": "Arroz", "precio": 2000},
                    {"id": 2, "nombre": "Aceite", "precio": 2500},
                    {"id": 3, "nombre": "Papa", "precio": 1800},
                    {"id": 4, "nombre": "Panela", "precio": 4000},
                    {"id": 5, "nombre": "Arroz", "precio": 2000},
                    {"id": 6, "nombre": "Aceite", "precio": 2500},
                    {"id": 7, "nombre": "Papa", "precio": 1800},
                    {"id": 8, "nombre": "Panela", "precio": 4000},
                    {"id": 9, "nombre": "Arroz", "precio": 2000},
                    {"id": 10, "nombre": "Aceite", "precio": 2500},
                    {"id": 11, "nombre": "Papa", "precio": 1800},
                    {"id": 12, "nombre": "Panela", "precio": 4000},
                    ]
        return jsonify({"datos": productos}), 200

class CategoriasGranosUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasCarnesUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasVerdurasUserControllers(MethodView):
    
    def post(self):
       pass