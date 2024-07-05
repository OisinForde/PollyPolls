from flask import Flask, render_template
import os

app = Flask(__name__,static_folder=os.path.abspath('clientend'),template_folder=os.path.abspath('clientend'))

@app.route('/')
def home():
    return "Welcome to PollyPolls!"

@app.route('/landing')
def landingPage():
    return render_template('landingPage/index.html')



if __name__ == '__main__':
    app.run(debug=True)