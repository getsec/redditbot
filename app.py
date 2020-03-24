from flask import Flask, render_template
import praw
import glob
import random
import os

app = Flask(__name__)

images = glob.glob("static/*.jpg")

@app.route('/')
def hello_world():
    random_image = random.choice(images)
    print(random_image)
    image = random_image.split('__')[1]
    subreddit = random_image.split('__')[0].split("static/")[1]
    full_path = os.path.join(random_image)
    print(full_path)
    html_title = random_image.split('__')[1].replace('_', ' ').rstrip('.jpg')
    print(html_title)
    return render_template('index.html', title=html_title, subreddit=subreddit.upper(), image=full_path)