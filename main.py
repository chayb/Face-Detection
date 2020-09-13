from flask import Flask
from app import views

app = Flask(__name__) # creates the web server

app.add_url_rule('/','base',views.base,methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True)