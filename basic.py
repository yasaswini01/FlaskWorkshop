from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'
@app.route('/<string:user>')
#for dynamic user
def hello_user(user):
	return 'hello '+user

if __name__=='__main__':
    app.run(debug=True)