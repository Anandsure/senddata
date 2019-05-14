from flask import Flask, flash, redirect, render_template, url_for, request
from flask_cors import CORS
app = Flask(__name__)

CORS(app)


@app.route('/print/name', methods=['POST'])
def get_names():
   if request.method == 'POST':
       names = request.get_json()
       print (names["text"])			
       return '', 200

if __name__=='__main__':
    app.run(debug=True)
    