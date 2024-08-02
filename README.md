# Claritas AI

WIP
**PLACED 1st out of 30 teams for the UTD 2024 summer AI internship/workshop**
project for the UTD 2024 summer AI internship/workshop

## Tech Stack
* Deployment
  * ngrok
* Frontend
  * HTML5 + CSS3 + JS
* Backend
  * Flask
  * Transformer NLP Model

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

## Frontend

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

## Research Paper
https://docs.google.com/document/d/1SFoNFnl0oVKxUKS3FH8rKBJN73elFlpQ/edit?usp=sharing&ouid=117610108974435331088&rtpof=true&sd=true
## Contributing
Aryan Bhattacharya, Daniel Hoffmaster, Peilun Li, Kyle Liu, Ishaant Majumdar, John Tad Tolbert
