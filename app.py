from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Okara, Pakistan',
    'salary' : 'Rs.150000'
  },
  {
    'id' : 2,
    'title' : 'Digital Marketing Manager',
    'location' : 'Lahore, Pakistan',
    'salary' : 'Rs.2150000'
  },
  {
    'id' : 3,
    'title' : 'Data Manager',
    'location' : 'Okara, Pakistan',
    'salary' : 'Rs.150000'
  },
  {
    'id' : 4,
    'title' : 'Graphic Designer',
    'location' : 'Okara, Pakistan',
    'salary' : 'Rs.150000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', 
                        jobs=JOBS,

                         company_name="Okara post")
  @app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
