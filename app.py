from flask import Flask
from flask.templating import render_template

#1 we made flask application
# a web server
#that writes html

app = Flask(__name__)

# if invoked from app.py then main
# else from somewhere else


#when homepage is accessed show "hello world"
#we registered our flask application
@app.route("/")
def hello_world():
  return render_template('home.html')


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
#debug means immediate changes in values in website
#if we created app.py now then run this app
