from app import app

PORT = 5000
DEBUG = True

#app.run(port=PORT, debug=DEBUG)
if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(port=PORT, debug=DEBUG)