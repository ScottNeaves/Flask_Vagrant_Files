from flask import Flask, request, redirect, url_for, render_template, session, jsonify
import os

app = Flask(__name__)
app.debug = True
app.secret_key=os.urandom(24) #for session management

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method=='GET':
		if 'username' in session:
			return render_template("index.html")
		else:
			return render_template("login.html")
	else: #request.method=='POST', user is logging in
		session['username'] = request.form['username']
		return render_template("index.html")	


if __name__ == "__main__":
	app.run(host='0.0.0.0')