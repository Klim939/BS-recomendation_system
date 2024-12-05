from flask import Flask, render_template, request
from werkzeug.serving import run_simple
from data_funcs import *

app = Flask(__name__, template_folder='templates')

data = load_data('purchases.json')
data_items = load_data('items.json')

@app.route('/')
def index():
    return "Hello world!"

@app.route('/<int:client_id>')
def rec(client_id):
    name = ''
    for i in data:
        if client_id == i['customer_id']:
            name = i['name']
    sizes = get_size(data, client_id)
    buys = get_buys(data, client_id)
    recomendation = recomend(data_items, sizes, buys)
    buys_by_size = get_buys_by_size(data_items, sizes)
    return render_template('index.html',
                           recommendations = recomendation,
                           items = buys_by_size,
                           sizes = sizes,
                           name = name)

if __name__ == '__main__':
    run_simple('localhost', 5000, app)