from flask import Flask, flash, redirect, render_template, url_for, request
from flask_cors import CORS
#import assistant
import json

app = Flask(__name__)

CORS(app)# to let the webapp know that this backend is ready to accept stuff.


@app.route('/print/name', methods=['POST', 'GET'])
def get_names():
   if request.method == 'POST':
       resp_json = request.get_json()
       print(resp_json['text'])
       
       #response = assistant.assistant(resp_json["test"])
       return json.dumps({"response": resp_json['text']}), 200

if __name__=='__main__':
    app.run(debug=True)
    
