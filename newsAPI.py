from flask import Flask, render_template, request, redirect, url_for, flash, Response
import os
import requests
import newsapi
from newsapi.newsapi_client import NewsApiClient

basedir = os.path.abspath(os.path.dirname(__file__))

from logging import DEBUG

app = Flask(__name__)  # create application object
app.config['SECRET_KEY'] = "b'\x92\xa7wF\x0b\x83\xb9\xcf1{\xba\xd4Ky\xa3\xe9 \xd1\x94\xd5\xa7-\xff\x1b'"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flask_one.db')


@app.route("/")
def home():
    return render_template("home.html")


def news_helper():
    """
    Fetch top news from newsapi and display them
    """

    country='country=fr&'

    topnews_url = 'https://newsapi.org/v2/top-headlines?' 'country=ng&' 'apiKey=25209a5d78924256b026ca496be2a0c8'

    # topnews_url = 'https://newsapi.org/v2/top-headlines?' + country + 'apiKey=25209a5d78924256b026ca496be2a0c8'

    open_news_page = requests.get(topnews_url).json()
    print(open_news_page)

    article = open_news_page["articles"]

    results = []

    for each in article:
        results.append(each['title'])

    description = []
    for each in article:
        description.append(each['description'])

    for i in range(len(results)):
        # print(i + 1, results[i])
        print(i + 1, results[i], ': ', description[i])

    return results


@app.route("/News", methods=['GET', 'POST'])
def news():
    return render_template('news.html', news_list=news_helper())


if __name__ == '__main__':
    app.run(debug=True)
