from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""
    
    return render_template("index.html")
    
    
@app.route("/goodbye")
def goodbye_page():
	"""Show goodbye page"""
	
	return render_template("goodbye.html")


@app.route("/application-form")
def get_app_form():
	"""Show the application form"""
	
	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def process_app():
	"""Process the application submission"""
	
	fname = request.form.get("fname")
	lname = request.form.get("lname")
	job = request.form.get("engjob")
	salary = int(request.form.get("salaryreq"))
	
	return render_template("application-response.html",
							firstname=fname, lastname=lname,
							job_title=job, salary=salary)
	



if __name__ == "__main__":
    app.run(debug=True)
