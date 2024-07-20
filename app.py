from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def data():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{a} + {b} = {a+b}"

@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from Flask!")

if __name__ == '__main__':
    app.run()
