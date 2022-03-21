from flask import Flask, render_template
import gunicorn
import werkzeug


app = Flask(__name__)

print('running')

@app.route ("/<string:page>", methods=['GET','POST'])
def index():
   return render_template('index.html')

@app.route ("/", methods=['GET','POST'])
def home():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)