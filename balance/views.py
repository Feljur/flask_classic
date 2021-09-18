from balance import app
from flask import render_template
from balance.models import ListaMovimientos
from flask import url_for
from datetime import date, datetime


def fecha_actual(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    fecha = "{} de {} de {}".format(day, month, year)

    return fecha



@app.route('/')
def inicio():
    lm = ListaMovimientos()
    lm.leer()
    now = datetime.now()
    return render_template('inicio.html', titulo="Balance de Cuentas", items=lm.movimientos, fecha_hoy = fecha_actual(now))