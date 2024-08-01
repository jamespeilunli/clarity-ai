from flask import Flask, jsonify, render_template, request, Response
from fetch_posts import fetch_recent_posts
from pyngrok import ngrok, conf
import os
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

    try:
        if input_type == "Account Handle":
            print("account handle", flush=True)
            mastodon_posts = fetch_recent_posts(user_input, 60)
            depression_score = multi_post.returnScore(mastodon_posts) * 100
            return {"message": "Success!", "input": data, "posts": mastodon_posts, "percentage": depression_score}, 200
        elif input_type == "Single Post":
            print("single post", flush=True)
            depression_score = single_post.returnScore(user_input) * 100
            return {"message": "Success!", "input": data, "percentage": depression_score}, 200
        else:
            return "invalid input type", 400
    except Exception as e:
        print("OMSDFS", e)
        return str(e), 500

@app.route('/api/add')
def data():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    response = jsonify({
        "received": {
            "a": a,
            "b": b,
        },
        "message": f"{a} + {b} = {a+b}",
    })
    response.status_code = 200

    return response

if __name__ == '__main__':
    # Set ngrok auth token
    conf.get_default().auth_token = os.environ.get("NGROK_AUTH_TOKEN")
    
    # Ensure no other ngrok sessions are running
    os.system("killall ngrok")
    
    # Start ngrok when the Flask app starts
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))
    
    # Start the Flask app
    app.run(debug=True, use_reloader=False)
