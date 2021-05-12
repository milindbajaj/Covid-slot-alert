from flask import Flask,render_template,request,jsonify
import requests
import json
from urllib.request import Request, urlopen

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods = [ "POST","GET"])
def home():
    if request.method == 'POST':
        pin = request.form.get('pin')
        date = request.form.get('date')
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(pin,date)
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.@ (X11; Linux x86 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
        }
        r=requests.get(url,headers=headers)
        data=r.json()
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run()