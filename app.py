from flask import Flask, jsonify, render_template, request
import fetch_mastodon_posts
import fetch_reddit_posts
import multi_post
import single_post

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/depression")
def depression():
    return render_template("depression.html")


@app.route("/anxiety")
def anxiety():
    return render_template("anxiety.html")


@app.route("/about-us")
def about_us():
    return render_template("about_us.html")


@app.route("/results")
def output_display():
    return render_template("results.html")


@app.route("/anxiety/results")
def anxiety_results():
    return render_template("anxiety_results.html")


@app.route("/model", methods=["POST"])
def model():
    data = request.get_json()
    user_input = data["input"]
    input_type = data["inputType"]
    print(f"app.py: /model was called; data == {data}")
    print(input_type)
    try:
        if input_type == "Account Handle":
            mastodon_posts = fetch_mastodon_posts.fetch_recent_posts(user_input, 60)
            multi_post.setModel("depression_model.pt")
            depression_score = multi_post.returnScore(mastodon_posts) * 100
            return {
                "message": "Success!",
                "input": data,
                "posts": mastodon_posts,
                "percentage": depression_score,
            }, 200
        elif input_type == "Single Post":
            depression_score = single_post.returnScore(user_input) * 100
            return {
                "message": "Success!",
                "input": data,
                "percentage": depression_score,
            }, 200
        elif input_type == "Mastodon Account Handle":
            mastodon_posts = fetch_mastodon_posts.fetch_recent_posts(user_input, 50)
            multi_post.setModel("anxiety_model.pt")
            anxiety_score = multi_post.returnScore(mastodon_posts) * 100
            return {
                "message": "Success!",
                "input": data,
                "posts": mastodon_posts,
                "percentage": anxiety_score,
            }, 200
        elif input_type == "Reddit Account Handle":
            mastodon_posts = fetch_reddit_posts.fetch_recent_posts(user_input, 50)
            multi_post.setModel("anxiety_model.pt")
            anxiety_score = multi_post.returnScore(mastodon_posts) * 100
            return {
                "message": "Success!",
                "input": data,
                "posts": mastodon_posts,
                "percentage": anxiety_score,
            }, 200
        else:
            return "invalid input type", 400
    except Exception as e:
        print(f"app.py: error: {e}")
        return str(e), 500


@app.route("/api/add")
def data():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    response = jsonify(
        {
            "received": {
                "a": a,
                "b": b,
            },
            "message": f"{a} + {b} = {a+b}",
        }
    )
    response.status_code = 200

    return response

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
