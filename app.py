from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Admin page
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Add product page
@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['product']
        price = request.form['price']

        print("New Product:", product_name)
        print("Price:", price)

        return redirect(url_for('admin'))

    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)