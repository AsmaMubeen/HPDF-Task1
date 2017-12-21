import requests, sys
from flask import Flask, request, redirect, render_template, make_response, abort


app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World - Asma"


@app.route('/authors',methods=['GET'])
def authors():
    authors = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {author['id']:{'name':author['name'],'count':0} for author in authors}
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('authors.html',users=users)


@app.route('/setcookie')
def setcookie():
	response = make_response('Setting cookie..')
	response.set_cookie('name','Asma')
	response.set_cookie('age','20')
	return response

@app.route('/getcookies')
def getcookie():
	if 'name' in request.cookies:
		name = request.cookies.get('name')
	else:
		return 'Cookie not found'

	if 'age' in request.cookies:
		age = request.cookies.get('age')
	else:
		return 'Cookie not found'

	return 'Name : ' + name + '<br>Age : ' + age


@app.route('/robots.txt')
def denyrequest():
	return redirect('http://httpbin.org/deny')


@app.route('/html')
def renderhtml():
	return render_template('Hasura.html')


@app.route('/input')
def textboxbinput():
	return render_template('TextInput.html')

@app.route('/output',methods = ['POST','GET'])
def log():
	if request.method == 'POST':
		data = request.form['input']
		print(data, file=sys.stdout)
	return 'Received data: '+ data +'<br>Logged the received data to stdout'



if __name__ == "__main__":
	app.run()
	