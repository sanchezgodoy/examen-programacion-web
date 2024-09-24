from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculodescuento', methods=['GET', 'POST'])
def calculoDescuento():
    if request.method == 'POST':
        nombre = request.form['nom1']
        edad = float(request.form['numero1'])
        tarros = float(request.form['numero2'])
        totalSinDescuento = tarros * 9000


        def descuento(edad):
            if edad >= 18 and edad <= 30:
                return 0.15  # Descuento del 15%
            elif edad > 30:
                return 0.25  # Descuento del 25%
            else:
                return 0.0  # Sin descuento para menores de 18

        totalDescuento = totalSinDescuento * descuento(edad)
        resultado = totalSinDescuento - totalDescuento

        return render_template('calculodescuento.html', resultado=resultado, nombre=nombre, edad=edad, tarros=tarros, totalSinDescuento=totalSinDescuento, descuento=descuento, totalDescuento=totalDescuento)
    return render_template('calculodescuento.html')


usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/nombreyedad', methods=['GET', 'POST'])
def nombre_y_edad():
    resultado = None  # Iniciar resultado como None
    if request.method == 'POST':
        nombre = request.form['nombre1']
        password = request.form['edad1']

        # Verificar las credenciales
        if nombre in usuarios and usuarios[nombre] == password:
            if nombre == 'juan':
                resultado = f'Bienvenido administrador {nombre}'
            elif nombre == 'pepe':
                resultado = f'Bienvenido usuario {nombre}'
        else:
            resultado = 'Usuario o contraseña incorrectos'

        return render_template('nombreyedad.html', resultado=resultado)
    return render_template('nombreyedad.html')


if __name__ == '__main__':
    app.run(debug=True)