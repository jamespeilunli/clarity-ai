from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model', methods=["POST"])
def model():
    data = request.get_json()
    user_input = data["input"]
    
    return jsonify({'message': f'Data "{user_input}" received successfully'})

@app.route('/api/add')
def data():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    response = jsonify({
        "recieved": {
            "a": a,
            "b": b,
        },
        "message": f"{a} + {b} = {a+b}",
    })
    response.status_code = 200

    return response

if __name__ == '__main__':
    app.run()
