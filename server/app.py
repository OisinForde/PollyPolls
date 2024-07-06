from flask import Flask, render_template
import os


app = Flask(__name__,static_folder=os.path.abspath('clientend'),template_folder=os.path.abspath('clientend'))

@app.route('/')
def home():
    return render_template('landingPage/index.html')

@app.route('/login')
def login():
    return render_template('loginPage/index.html')

@app.route('/register')
def register():
    return render_template('registerPage/index.html')



if __name__ == '__main__':
    app.run(debug=True)