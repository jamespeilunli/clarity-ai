# Clarity AI

This natural language processing AI/ML project leverages sentiment analysis to detect depression and anxiety from personal, text-based social media posts in English. It utilizes binary classification with transformers to accurately provide insights on potential mental health indicators based on users' content. 

We deployed our project on an AWS EC2 instance. Check it out at [ai-clarity.org](https://ai-clarity.org/)!

Our team of six high schoolers developed this as our project for the 2024 summer UTD Deep Dive AI Workshop. Our project placed first out of the 30 teams attending the workshop!

**DISCLAIMER:** The output of our AI models are for informational purposes only and does not provide medical advice or diagnosis. Always consult a qualified healthcare provider for any concerns regarding mental health.

## Contributors

Aryan Bhattacharya, Daniel Hoffmaster, Peilun Li, Kyle Liu, Ishaant Majumdar, John Tad Tolbert

## Tech Stack

* **Deployment**
  * AWS EC2
  * Cloudflare
* **Frontend**
  * HTML5 + CSS3 + JS
* **Backend**
  * Flask
  * Mastodon.py
  * PyTorch + Hugging Face transformers

## Code Specifics

### Backend - NLP Models

* **Single Post Depression Detection** (`depression_single_post_model.pt`): Uses a pre-trained BERT model ([bert-base-cased](https://huggingface.co/docs/transformers/en/model_doc/bert)) followed by a small MLP with a sigmoid activation. Optimizations include L2 regularization and dropout layers. `single_post.py` handles tokenization and inference for individual post analysis.

* **Multi-Post Depression Detection** (`depression_model.pt`): Utilizes TinyBERT ([bert-tiny](https://huggingface.co/prajjwal1/bert-tiny)) for vectorizing each post to a 128-dimensional vector. The vectors are processed sequentially by an LSTM layer, and the final output is classified via a neural network and sigmoid activation to generate a depression score. `multi_post.py` handles tokenization and sequential inference across multiple posts.

* **Anxiety Detection** (`anxiety_model.pt`): Follows the same architecture as `depression_model.pt`, trained on anxiety-specific data. It also utilizes `multi_post.py` for analysis of sequential posts.

**For a closer look:** The `model` branch contains our training code, datasets, and documentation of model experiments, detailing variations in architecture, hyperparameters, and optimizations.

### Backend - Social Media Post Retrieval

* **Mastodon Posts**: We use the [Mastodon.py API](https://mastodonpy.readthedocs.io/en/stable/) in `fetch_mastodon_posts.py` to retrieve user posts. Basic input handling and text parsing (e.g., HTML tag removal, hashtag preservation) are applied.

* **Reddit Posts**: The Reddit API is employed in `fetch_reddit_posts.py` to retrieve posts by user.

### Frontend

The website features a responsive, user-friendly interface designed for an engaging experience.

- **Interactive UI Elements**: Clickable cards and interactive forms.
- **Modern Design**: Incorporates animations and a clean aesthetic for an appealing look.
- **Responsive Layout**: Ensures usability across devices and screen sizes.

*References*:  
- Hyperplexed Pen on CodePen: [CodePen 1](https://codepen.io/Hyperplexed/full/MWQeYLW), [CodePen 2](https://codepen.io/Hyperplexed/pen/YzeOLYe)  
- AuthKit: [AuthKit](https://www.authkit.com/)

## Running

### Setup

Create a `.env` file:
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

Our project is hosted on an AWS EC2 instance and is accessible via our Cloudflare domain at [ai-clarity.org](https://ai-clarity.org/).
