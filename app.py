from flask import Flask, jsonify, render_template, request
from fetch_posts import fetch_recent_posts
import multi_post
import single_post 

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
    print("/model called, input", user_input, input_type, flush=True)

    if input_type == "Account Handle":
        print("account handle", flush=True)
        mastodon_posts = fetch_recent_posts(user_input, 60)
        depression_score = multi_post.returnScore(mastodon_posts) * 100
        return jsonify({'message': f'Data "{user_input}" of type "{input_type}" received successfully.', 'Posts': mastodon_posts, 'percentage': depression_score})
    elif input_type == "Single Post":
        print("single post", flush=True)
        depression_score = single_post.returnScore(user_input) * 100
        return jsonify({'percentage': depression_score})

    return jsonify({'message': 'Error', 'percentage': 'Error'})

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
