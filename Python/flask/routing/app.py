from flask import Flask
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route("/")
def home():
    return "Hello, Flask!"


if __name__=="__main__":
    app.run()
