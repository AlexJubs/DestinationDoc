#app.py

from flask import Flask, request #import main Flask class and request object
import requests
import json
import pprint

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
    url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('physiotherapy', '47.602038', '-122.333964')
    print(url)
    re = requests.get(url)
    returning = json.loads(re.text)
    #return returning['resourceSets']['0']['estimatedTotal']
    print(type(returning['resourceSets'][0]['resources']))
    print(returning['resourceSets'][0]['resources'][0]['name'])
    for i in len(returning['resourceSets'][0]['resources']):
    	print(returning['resourceSets'][0]['resources'][i]['name'])
    return str(returning['resourceSets'][0]['estimatedTotal'])

@app.route('/form-example')
def formexample():
    return 'Todo...'

@app.route('/json-example')
def jsonexample():
    return 'Todo...'

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
