from flask import Flask

#1 we made flask application

app = Flask(__name__)

# if invoked from app.py then main
# else from somewhere else


#when homepage is accessed show "hello world"
#we registered our flask application
@app.route("/")
def hello_world():
  return f"hello world"


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
#debug means immediate changes in values in website
#if we created app.py now then run this app
