from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

