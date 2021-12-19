from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods = ["GET", "POST"])
def search():
    API_TOKEN = "SUA_API_TOKEN"
    city = request.form["city"]
    state = request.form["state"]

    url_api = f"https://api.brasil.io/v1/dataset/covid19/caso_full/data/?city={city}&state={state}&page_size=1"
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "User-Agent": "python-urlib/brasilio-client-0.1.0"
    }

    results = []  # Zera o array

    try:
        res = requests.get(url_api, headers=headers)
        results = res.json()['results']        
    except:
        pass

    if len(results):
        result = {
            "city": results[0]["city"],
            "state": results[0]["state"],
            "date": results[0]["date"],
            "last_available_confirmed": results[0]["last_available_confirmed"],
            "last_available_deaths": results[0]["last_available_deaths"],
            "estimated_population": results[0]["estimated_population"]
        }
    else:
        result = { }

    return render_template("result.html", result = result)

if __name__ == "__main__":
    app.run(debug = True)