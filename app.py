from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb+srv://shivamchand2013_db_user:9431176854ss@cluster1.eyur0v0.mongodb.net/kanha?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    products = mongo.db.products.find()
    return render_template('admin.html', products=products)

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():

    if request.method == 'POST':

        product_name = request.form['product']
        price = request.form['price']

        mongo.db.products.insert_one({
            'name': product_name,
            'price': price
        })

        return redirect(url_for('admin'))

    return render_template('add_product.html')

@app.route('/delete-product/<product_id>')
def delete_product(product_id):

    mongo.db.products.delete_one({
        '_id': ObjectId(product_id)
    })

    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)