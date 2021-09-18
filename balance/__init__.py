from flask import Flask

FICHERO = 'data/movimientos.csv'
app = Flask(__name__, static_folder='../static')

from balance import views