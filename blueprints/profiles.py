from flask import Blueprint, render_template, request
from newsapi.newsapi_client import NewsApiClient
import requests
import json

profiles = Blueprint('profiles', __name__,
                        url_prefix='/',
                        template_folder='templates',
                        static_folder='static', static_url_path='assets')


@profiles.route('/raiden/')
def raiden():
    return render_template("profiles/raiden.html", news='')


@profiles.route('/raiden/results/', methods=['POST'])
def get_results():
    keyword = request.form['keyword']  # getting input from user

    news = newsapi.get_top_headlines(q=keyword,
                                     # sources='bbc-news,the-verge',#optional and you can change
                                     # category='business', #optional and you can change also
                                     language='en',  # optional and you can change also
                                     country='in')
    # print(news['articles'])
    return render_template('profiles/raiden.html', news=news['articles'])

@profiles.route('/paul/')
def paul():
    return render_template("profiles/paul.html")


@profiles.route('/armaan/')
def armaan():
    return render_template("profiles/armaan.html")


@profiles.route('/kurtis/')
def kurtis():

    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
    querystring = {"category":"sciencenature","limit":"1"}
    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    print(output)
    return render_template("profiles/kurtis.html", question=output)