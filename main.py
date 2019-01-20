from flask import Flask, render_template, request
from webapp2 import *
import pymysql


app = Flask(__name__)

@app.route('/')
def index():
    title='Anime Land'
    page="index"
    return render_template('index.html', title=title, page=page)

@app.route('/anime-series/')
def anime_series():
    title='Anime Series'
    page="anime series"
    return render_template('series.html', title=title, page=page)

@app.route('/anime/special-episodes/')
def special_episodes():
    title='Special Episodes'
    page="special episodes"
    return render_template('series.html', title=title, page=page)

@app.route('/anime/ova/')
def ova():
    title='Ova'
    page="ova"
    return render_template('series.html', title=title, page=page)

@app.route('/anime/movies/')
def movies():
    title='Movies'
    page="movies"
    return render_template('series.html', title=title, page=page)

@app.route('/anime/this-season/')
def season():
    title='This Season Anime'
    page="season"
    return render_template('series.html', title=title, page=page)

@app.route('/anime/episodes/')
def episodes():
    title='episodes'
    page='episodes'
    return render_template('series.html', title=title, page=page)

@app.route('/anime/episodes/watch/')
def wath():
    title=request.args.get('title', '')
    return render_template('watch.html', title=title)

@app.route('/manga-series/')
def manga():
    title="Manga"
    page="manga"
    return render_template('series.html', title=title, page=page)

@app.route('/manga/one-shot/')
def one_shot():
    title='One Shot'
    page='one shot'
    return render_template('series.html', title=title, page=page)

@app.route('/manga/chapters/')
def chapters():
    title="Chapters"
    page="chapters"
    return render_template('series.html', title=title, page=page)

@app.route('/manga/chapters/read/')
def read():
    title=request.args.get('title', '')
    return render_template('read.html', title=title)

@app.route('/anime-news/')
def anime_news():
    title=request.args.get('title', '')
    return render_template('news.html', title=title)

@app.route('/manga-news/')
def manga_news():
    title=request.args.get('title', '')
    return render_template('news.html', title=title)

@app.route('/register/')
def register_page():
    title='Anime Land'
    page="register"
    return render_template('create-account.html', title=title, page=page)

@app.route('/login/')
def login_page():
    title = 'Anime Land'
    page = 'login'
    return render_template('login.html', title = title, page = page)

@app.route('/register/')
def register():
    return None

@app.route('/login/')
def login():
    return None

if __name__ == '__main__':
    app.run(debug=True)

