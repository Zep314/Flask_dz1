import os
from flask import Flask, render_template, send_from_directory
from database.base import data_base

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/catalog/')
def catalog():
    context = {'catalog': data_base().get_data()}
    return render_template('catalog.html', **context)


@app.route('/catalog/<my_catalog_item>/')
def catalog_item(my_catalog_item=''):
    context = {'my_catalog_item': {'name': 'Нет данных', 'price': 0, 'color': 'Нет данных'}}
    for item in data_base().get_data():
        if item['name'] == my_catalog_item:
            context = {'my_catalog_item': {'name': item['name'], 'price': item['price'], 'color': item['color']}}
            break
    return render_template('catalog_item.html', **context)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)
