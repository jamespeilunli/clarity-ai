# Clarity AI

WIP

This natural language processing AI/ML project leverages sentiment analysis to detect depression from personal, text-based social media posts in English. It utilizes binary classification with transformers to accurately identify potential signs of depression in user content. 

We deploy our project as a Flask web app using ngrok (permanent url may be provided soon).

Our team of six high schoolers developed this as our project for the 2024 summer UTD Deep Dive AI Workshop. Our project placed first out of the 30 teams attending the workshop!

**DISCLAIMER:** The output of our AI model is for informational purposes only and does not provide medical advice or diagnosis. Always consult a qualified healthcare provider for any concerns regarding mental health.

## Contributors

Aryan Bhattacharya, Daniel Hoffmaster, Peilun Li, Kyle Liu, Ishaant Majumdar, John Tad Tolbert

## Tech Stack

* Deployment
  * ngrok
* Frontend
  * HTML5 + CSS3 + JS
* Backend
  * Flask
  * Mastodon.py
  * PyTorch + Hugging Face transformers

## Code Specifics

### Backend - Our NLP Models

* for a single social media post (stored in `single_post_model.pt`): a pre-trained BERT ([bert-base-cased](https://huggingface.co/docs/transformers/en/model_doc/bert)) fed into a small MLP and then a sigmoid activation. There are also various optimizations such as L2 regularization and dropout layers. `single_post.py` tokenizes a single post content and then performs inference on the tokens with this model. 

* for multiple social media posts (stored in `multi_post_model.pt`): a pre-trained BERT model named TinyBert ([bert-tiny](https://huggingface.co/prajjwal1/bert-tiny)) processes each tweet into a size 128 vector.  The output of the BERTs processing each tweet is partitioned into multiple sections. Each of these sections is put through an LSTM where each timestamp takes the vector output of the BERT for one tweet as input. The output is then condensed into a single value through a small neural network. This value is then put through a sigmoid function to get one percentage for the depression value. `multi_post.py` tokenizes each post in a list of posts then performs inference on the tokens with this model. 

**Explore the `model` branch** and its associated PR to view our training code for the final models. `model` also contains our parsed datasets and details of various model experiments, including those with different architectures, models, hyperparameters, and optimizations for accuracy and efficiency.

### Backend - Social Media Post Retrieval

We use the [Mastodon.py API](https://mastodonpy.readthedocs.io/en/stable/) in `fetch_posts.py` to retrieve users’ past Mastodon posts for our multi-post model to later analyze. We also perform basic input handling as well as parsing of the retrieved mastodon posts (e.g. removing html tags and preserving hashtags).

### Frontend

The site features interactive elements and a visually appealing design to enhance user experience.

*References*:
The project was inspired by and built using concepts from the following resources:

 * Hyperplexed Pen on CodePen (https://codepen.io/Hyperplexed/full/MWQeYLW)
 * Hyperplexed Pen on CodePen pt. 2 (https://codepen.io/Hyperplexed/pen/YzeOLYe)
 * AuthKit (https://www.authkit.com/)
 * Project Features

*Interactive UI Elements*: The website includes interactive elements such as clickable cards that reveal input forms.

*Stylish Design*: Utilizes modern design principles and animations to create a visually appealing interface.

*Responsive Layout*: Ensures a consistent experience across different devices and screen sizes.

## Running

### Setup

Write a `.env`:
```
MASTODON_EMAIL=XXXXXXXXXXXXXXXXXXXXX
MASTODON_PASSWORD=XXXXXXXXXXXXXXXXXXXXX
MASTODON_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
MASTODON_CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Install dependencies: `pip3 install -r requirements.txt`

### Local Development

```bash
python3 app.py
```

The local server should automatically update on reload when you make changes to the code.

### Web Deployment

Make sure you have ngrok installed: [download page](https://ngrok.com/download)

```bash
# start gunicorn WSGI local server
gunicorn -b 127.0.0.1:5000 app:app
```
in a new terminal:
```bash
# deploy port 5000 to ngrok
ngrok http 5000
```
