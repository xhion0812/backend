from flask.views import MethodView
from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify, request, flash
import MySQLdb.cursors
import bcrypt
import time
import re

app = Flask(__name__)


app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todito'

mysql = MySQL(app)
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
        #salt = bcrypt.gensalt()
        salt = bcrypt.gensalt()
        print("PASSWORD LISTA")
        hash_password = bcrypt.hashpw(bytes(str(password), encoding='utf-8'), salt)
        print("PASSWORD ",hash_password)
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO registro (nombres, apellidos, documento, direccion, telefono, correo, pass) VALUES(%s, %s, %s, %s, %s, %s, %s)',(nombres, apellidos, documento, direccion, telefono, correo, hash_password))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"login ok": True, "nombres": nombres, "apellidos": apellidos, "cedula": documento, "direccion": direccion, "telefono": telefono, "correo": correo}), 200

class InicioSesionUserControllers(MethodView):

    def post(self):
        datos = ""
        time.sleep(3)        
        content = request.get_json()
        correo = content.get("email")
        password = content.get("password")
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        cursor = mysql.connection.cursor()
        cursor.execute("""SELECT nombres, apellidos, pass, documento, direccion, telefono, correo FROM registro WHERE correo = %s""", ([correo]))
        datos = cursor.fetchall()
        datos = datos[0]
        print(datos)
        print("DATO DE LA CONSULTA",datos[6])
        email = datos[6]
        clave = datos[2]
        print("DATOS CONTRASEÑA ",datos[2])
        user = {}
        user[email] = {"contraseña":clave}
        print("SE IMPRIME LOS DATOS DE USER ",user[email])
        print("SE IMPRIME GET ", user.get(email))
        if user.get(correo):
            passwordUser= user[correo]["contraseña"]
            print("DEPUES DEL IF ", passwordUser)
            if bcrypt.checkpw(bytes(str(password), encoding='utf-8'),passwordUser.encode('utf-8')):
            #if bcrypt.checkpw(bytes(str(password), encoding='utf-8'),passwordUser.encode('utf-8')):
                
                #return print("ESTAMOS AQUI ")
                return jsonify({"auth": True, "nombres":datos[0], "apellidos":datos[1], "documento":datos[3], "direccion":datos[4], "telefono":datos[5], "token":token}), 200    
            else:
               return jsonify({"auth":False}), 403
        else:
            return jsonify({"auth":False}), 401
"""        
        if bcrypt.check_password_hash(rv['password'], password):
            access_token = create_access_token(identity = {'nombres': rv['nombres'], 'apellidos': rv['apellidos'], 'email': rv['email']})
            result = jsonify({"token":access_token})
        else:
            result = jsonify({"Error":"ivalido el nombre o contraseña"})
        
        return result"""
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