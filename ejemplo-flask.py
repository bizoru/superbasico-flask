from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


imagen_gato1 = "https://www.petfinder.com/wp-content/uploads/2012/11/91615172-find-a-lump-on-cats-skin-632x475.jpg"
imagen_gato2 = "http://r.ddmcdn.com/s_f/o_1/cx_462/cy_245/cw_1349/ch_1349/w_720/APL/uploads/2015/06/caturday-shutterstock_149320799.jpg"

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/ricardo')
def saludo_ricardo():
    return "<h1>Hello Ricardo</h1> <img src='{}'>".format(imagen_gato1)

@app.route('/saludar/steven')
def steven():
    return "<h1>Hello Steven</h1> <img src='{}'>".format(imagen_gato2)

@app.route('/saludar')
def saludar():
    nombre = request.args.get('nombre')
    edad = request.args.get('edad')
    resultado_edad = ""

    if int(edad) > 10:
        resultado_edad = "Ya eres mayor de diez anos!!"

    if int(edad) == 30:
        resultado_edad = "Ya vas por el tercer piso"

    return render_template("resultado.html",nombre=nombre,resultado=resultado_edad)

@app.route('/plantilla')
def plantilla():
    return render_template("login.html")



@app.route('/login', methods=['POST', 'GET'])
def login():
    #error = None
    #if request.method == 'POST':
    #    if valid_login(request.form['username'],
    #                   request.form['password']):
    #        return log_the_user_in(request.form['username'])
    #    else:
    #        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
