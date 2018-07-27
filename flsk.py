from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('ma1n.html')


@app.route('/scirc')
def scirc():
    if 'rad' in request.args and request.args['rad']:
        q = float(request.args['rad'])
        a = 3.14 * (q**2)
        b = 'Площадь данной окружности равна '
        c = ' см^2.'
    else:
        a = 'Введите значение'
        b = ''
        c = ''
    return render_template('scirc.html', txt = b, scrc = a, txtsm = c)


@app.route('/lcirc')
def lc():
    if 'rad1' in request.args and request.args['rad1'].isdigit() == True:
        q1 = int(request.args['rad1'])
        a1 = 3.14 * q1
        a1 = a1 * 2
        b1 = 'Длина данной окружности равна '
        c1 = ' см.'
    else:
        a1 = 'Введите значение!'
        b1 = ''
        c1 = ''
    return render_template('lcirc.html', txt = b1, lcrc = a1, txtsm = c1)
@app.route('/ssq')
def ssq():
    if 'int' in request.args and 'stepen' in request.args and request.args['int'].isdigit() == True and request.args['stepen'].isdigit() == True:
        w1 = int(request.args['int'])
        e1 = int(request.args['stepen'])
        r = w1 ** e1
        k1 = ''
    else:
        r = ''
        k1 = 'Введите значения!'
    return render_template('ssq.html', txt=k1, ssq=r)


app.run(debug=True, port=8080)