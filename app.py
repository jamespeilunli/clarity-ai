from flask import Flask, jsonify, render_template, request
from fetch_posts import fetch_recent_posts
from multi_post_model import get_depression_score

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def output_display():
    return render_template('results.html')

@app.route('/model', methods=["POST"])
def model():
    data = request.get_json()
    user_input = data["input"]
    input_type = data["inputType"]

    if input_type == "Account Handle":
        mastodon_posts = fetch_recent_posts(user_input, 10)
        depression_score = get_depression_score(mastodon_posts)
    
    return jsonify({'message': f'Data "{user_input}" of type "{input_type}" received successfully.', 'Posts': mastodon_posts, 'percentage': depression_score})

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
    app.run(debug=True)
