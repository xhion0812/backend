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
    """
        Example Login
    """
    """def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        if (email == "test@gmail.com" and password == "12345"):
            return jsonify({"auth": True, "name": "Pepe Perez", "token": token}), 200
        return jsonify({"auth": False}), 401
    """    
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
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1000),'email': correo }, KEY_TOKEN_AUTH , algorithm="HS256")
                print("Correo",correo)
                return jsonify({"Status": "Login exitoso", "token": encoded_jwt}), 200               
                
                #return jsonify({"auth": True, "nombres":datos[0], "apellidos":datos[1], "documento":datos[3], "direccion":datos[4], "telefono":datos[5], "token":token}), 200    
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
               return jsonify({"Status": "Autorizado por token", "correoextraido": data.get("email"), "tabla": {"id":1, "nombre":"Pollo Campecino", "precio":15000, "url": "https://revistalabarra.com/guia/files/classifieds/5424-8182.jpg"}}), 200
            except:
                    return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        #return jsonify({"Status": "No ha enviado un token"}), 403 
        productos = [{"id": 1, "nombre": "Pollo Campecino", "precio": 15000, "url": "https://revistalabarra.com/guia/files/classifieds/5424-8182.jpg"},
                    {"id": 2, "nombre": "Carne de Espaldilla", "precio": 18900, "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4wklKrdd6pNCplsDVQSNp54OQRDCwaJvx5Q&usqp=CAU"},
                    {"id": 3, "nombre": "Papa Pastusa", "precio": 1800, "url": "https://justoyfresco.com/wp-content/uploads/2020/05/Papa-Pastusa.jpg"},
                    {"id": 4, "nombre": "Panela Valluna", "precio": 4999,"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfQoo-RUGNCUgfXo8vIZj0zrdjzWmBBJWdxw&usqp=CAU"},
                    {"id": 5, "nombre": "Arroz Diana", "precio": 2800, "url": "https://jumbocolombiafood.vteximg.com.br/arquivos/ids/3510553-1000-1000/7702511002933.jpg?v=637273105687100000"},
                    {"id": 6, "nombre": "Aceite Oliosoya", "precio": 25000, "url": "https://m.media-amazon.com/images/I/41ACSASszPL.jpg"},
                    {"id": 7, "nombre": "Lentejas", "precio": 1800,"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4wklKrdd6pNCplsDVQSNp54OQRDCwaJvx5Q&usqp=CAU"},
                    {"id": 8, "nombre": "Frijoles", "precio": 2200, "url": "https://images-na.ssl-images-amazon.com/images/I/51Ngv8BjnML._AC_.jpg"},
                    {"id": 9, "nombre": "Spaguetis", "precio": 1200, "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVCRlkY-HCKgNxyTQNCEjc_3HnbEpX36PTJA&usqp=CAU"},
                    {"id": 10, "nombre": "verdura Verdes", "precio": 3000, "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMOifhQWgeAxYSvz86fsjLunCN25tTOMlTOA&usqp=CAU"},
                    {"id": 11, "nombre": "Frutas Rojas", "precio": 5800, "url": "https://estaticos.miarevista.es/media/cache/760x570_thumb/uploads/images/article/577247a7a1119be306b5a0ef/zarzamora-interior.jpg"},
                    {"id": 12, "nombre": "Hortalizas", "precio": 3300, "url": "https://universidadagricola.com/wp-content/uploads/2018/07/img_5b5a117b78e06.png"}]
                  
 
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