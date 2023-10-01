# Import the Flask and render_template classes from the Flask module
from flask import Flask
from flask.templating import render_template
from flask import jsonify

# Create a Flask application
app = Flask(__name__)

#this jobs input can be taken from mysql
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru,India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Front-end engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 3,
    'title': 'Data engineer',
    'location': 'San Fransisco',
    'salary': '$120,000'
}, {
    'id': 4,
    'title': 'Data scientist',
    'location': 'Mumbai'
}]


# Define a route for the homepage ("/") and associate it with a function
@app.route("/")
def hello_world():  #html route
  # Return the result of rendering the "home.html" template
  return render_template('home.html', jobs=JOBS, company_name="COCONUTs")


@app.route("/api/jobs")  #json route
def list_jobs():
  return jsonify(JOBS)


# Check if the script is being run as the main program
if __name__ == "__main__":
  # Run the Flask application on all available network interfaces (0.0.0.0)
  # with debugging enabled (debug=True)
  app.run(host='0.0.0.0', debug=True)
