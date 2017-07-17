from flask import Flask, render_template, request, redirect
import requests

app = Flask("MyApp")

@app.route("/")
def welcome():
  return render_template("name.html")

@app.route("/whoruntheworld/", methods=["POST"])
def check_name():
	print request.form
	if request.form["firstname"]:
		name = request.form["firstname"]
		return redirect("/whoruntheworld/{}".format(name))
	else:
		return render_template("hello.html", name=None)

@app.route("/sign_up", methods=["POST"])
def send_message():
  email = request.form["email_address"]
  name = request.form["first_name"]
  print email
  print name
  return requests.post(
		"https://api.mailgun.net/v3/[YOURDOMAINNAME]/messages",
		auth={"api", "[YOUR_API_KEY]"},
		data={"from": "Merve <cfg@merve.com>",
					"to": email,
					"subject": "Hi!",
					"text": "Hello {}, thank you for signing up!".format(name)})

@app.route("/whoruntheworld/<name>")
def girls(name=None):
  return render_template("hello.html", name=name)

app.run(debug=True)

