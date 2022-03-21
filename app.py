from flask import Flask, render_template
import gunicorn
import werkzeug


app = Flask(__name__)

print('running')

@app.route ("/<string:page>", methods=['GET','POST'])
def index(page):
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)