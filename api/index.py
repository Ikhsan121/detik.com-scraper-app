import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def detik_popular():
    html_doc = requests.get("https://www.detik.com/terpopuler")

    soup = BeautifulSoup(html_doc.text, 'html.parser')
    popular_area = soup.find(attrs={'class': 'grid-row list-content'})

    images = popular_area.find_all(attrs={'class': 'media__image'})

    return render_template('index.html', images=images)

