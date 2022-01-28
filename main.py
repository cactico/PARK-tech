# import "packages" from flask
import json

# import app as app
import requests
from flask import render_template, request, Flask
from __init__ import app
from newsapi.newsapi_client import NewsApiClient
from crud.app_crud import app_crud
from blueprints.profiles import profiles

app.register_blueprint(app_crud)
app.register_blueprint(profiles)
# create a Flask instance

yourAPIKEY = '8169dc4f99474483ab5999bc2c761381'  # write your API key here
newsapi = NewsApiClient(api_key=yourAPIKEY)

# connects default URL to render index.html


@app.route('/')
def index():
    return render_template("index.html")



# runs the application on the development server
fivestars_list = []
fourstars_list = []
threestars_list = []
twostars_list = []
onestar_list = []

# def averagecalc():
#    average = 0
#    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
#    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
#    if total != 0:
#        average = sum / total


@app.route('/rating_test/')
def rating_test():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/fivestars', methods=['GET', 'POST'])
def fivestars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            fivestars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/fourstars', methods=['GET', 'POST'])
def fourstars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            fourstars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/threestars', methods=['GET', 'POST'])
def threestars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            threestars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/twostars', methods=['GET', 'POST'])
def twostars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            twostars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/onestar', methods=['GET', 'POST'])
def onestar():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            onestar_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/databases/')
def databases():
    return render_template("Databases/databases.html")


@app.route('/search/')
def search():
    return render_template("search.html")


@app.route('/isbn/')
def isbn():
    return render_template("isbn.html")


@app.route('/database1/')
def database1():
    return render_template("Databases/database1.html")


@app.route('/moreinfo/')
def moreinfo():
    return render_template("moreinfo.html")


@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/register/')
def register():
    return render_template("register.html")


@app.route('/error/')
def error():
    return render_template("error.html")


@app.route('/random')
def random():
    return render_template("randombook.html")
# @app.route('/crud')
# def crud():
#     """obtains all Users from table and loads Admin Form"""
#     return render_template("crud/templates/crud/crud.html")


@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.form:
        resultA = request.form.get("input1")
        x = '{ "0":"Data A", "1":"Data B", "2":"Data C", "3":""}'
        # parse x:
        y = json.loads(x)
        myoutput = y[resultA]
        return render_template("ratings/rating_test.html", output=myoutput)
    return render_template("ratings/rating_test.html")


@app.route('/bookname', methods=['GET', 'POST'])
def bookname():
    if request.form:
        name = request.form.get("search")
        if len(name) != 0:
            return render_template("ratings/rating_test.html", rate="Rating for: ", thename=name)
    return render_template("ratings/rating_test.html")

if __name__ == "__main__":
    app.run( debug=True)