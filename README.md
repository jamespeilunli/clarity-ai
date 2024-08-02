# Claritas AI

WIP

This natural language processing AI/ML project leverages sentiment analysis to detect depression from social media posts. It utilizes binary classification with transformers to accurately identify potential signs of depression in user content. 

We deploy our project as a Flask web app using ngrok (permanent url may be provided soon).

Our team of six high schoolers developed this as our project for the 2024 UTD Deep Dive AI Workshop.

**DISCLAIMER:** The output of our AI model is for informational purposes only and does not provide medical advice or diagnosis. Always consult a qualified healthcare provider for any concerns regarding mental health.

## Tech Stack

* Deployment
  * ngrok
* Frontend
  * HTML5 + CSS3 + JS
* Backend
  * Flask
  * Mastodon.py
  * PyTorch + Hugging Face transformers

## Code Structure

## Running

### Setup

Write a `.env`:
```
NGROK_AUTH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
MASTODON_EMAIL=XXXXXXXXXXXXXXXXXXXXX
MASTODON_PASSWORD=XXXXXXXXXXXXXXXXXXXXX
MASTODON_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
MASTODON_CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Install dependencies: `pip3 install -r requirements.txt`

### Local Development

```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run # go to the linked local server this gives you
```
The local server should automatically update on reload when you make changes to the code.

### Web Deployment

Make sure you have ngrok installed: [download page](https://ngrok.com/download)

`python3 app.py`

## Code Specifics

### Backend - Our NLP Models

Check out the `model` branch and its corresponding PR to see our parsed datasets as well as our many model experiments (e.g. with different architectures, models, hyperparameters, accuracy optimizations, efficiency optimizations)!

### Backend - Social Media Post Retrieval

### Frontend

The site features interactive elements and a visually appealing design to enhance user experience.

*References*
The project was inspired by and built using concepts from the following resources:

 * Hyperplexed Pen on CodePen (https://codepen.io/Hyperplexed/full/MWQeYLW)
 * Hyperplexed Pen on CodePen pt. 2 (https://codepen.io/Hyperplexed/pen/YzeOLYe)
 * AuthKit (https://www.authkit.com/)
 * Project Features

*Interactive UI Elements*: The website includes interactive elements such as clickable cards that reveal input forms.

*Stylish Design*: Utilizes modern design principles and animations to create a visually appealing interface.

*Responsive Layout*: Ensures a consistent experience across different devices and screen sizes.

