from flask import Flask, render_template
import urllib.request, json
import requests
import os
app = Flask(__name__)

@app.route("/")
def get_dict():
    url = "https://reqres.in/api/users?page=2"

    #response = urllib.request.urlopen(url)
    response = requests.get("https://reqres.in/api/users?page=2")
    data = response.json()
    response_list=data["data"]
    response_dict={}
    for i in response_list:
        response_dict[i["email"]]=i


    return (response_dict)
if __name__ == '__main__':
    app.run()