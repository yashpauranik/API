from flask import Flask, render_template
import urllib.request, json
import requests
import os
app = Flask(__name__)
def getResult():
    def get_requestDetails():
        requestDict = { "url" : "https://reqres.in/api/users?page=2",
                        "method" : "get"
                        }
        return requestDict
    def getRsponse():
        requestDict = get_requestDetails()
        if (requestDict["method"]=="get"):
            response = requests.get(requestDict["url"])
        else :
            print("will implement later")
        return response


    def parseResponse():
        data = getRsponse()
        data = data.json()
        response_list=data["data"]
        response_dict={}

        for i in response_list:
            response_dict[i["email"]]=i
        return (response_dict)
    return parseResponse()


@app.route("/")
def getData() :
    return getResult()
if __name__ == '__main__':
    app.run()