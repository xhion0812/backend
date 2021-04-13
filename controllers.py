from flask.views import MethodView
from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify, request, flash
import jwt
import datetime
import MySQLdb.cursors
import bcrypt
from config import KEY_TOKEN_AUTH
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
    def get(self):
        pass


    
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

        print("ESTE ES EL CORREO: ",correo)
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

                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5000),'correo': correo }, KEY_TOKEN_AUTH , algorithm="HS256")
                print("Correo",correo)

                return jsonify({"auth": True, "nombres":datos[0], "apellidos":datos[1], "documento":datos[3], "direccion": datos[4], "telefono":datos[5], "correo":datos[6], "token": encoded_jwt}), 200                   
            else:
               return jsonify({"auth":False}), 403
        else:
            return jsonify({"auth":False}), 401




class TablaControllers(MethodView):
    def get(self):
        
        if(request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------",token[1])

            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                productos = ""
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT id, nombre, img, precio FROM productos')
                productos = cursor.fetchall()
                print("ESTOS SON TODOS LOS PRODUCTOS DE LA BD: ",productos)
        
                return jsonify(
                    {"Status": "Autorizado por token", "correoextraido": data.get("email"), "datos":productos}), 200
            except:

                    return jsonify({"Status": "TOKEN NO VALIDO"}), 403
 
    

class CategoriasGranosUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasCarnesUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasVerdurasUserControllers(MethodView):
    
    def post(self):
       pass
