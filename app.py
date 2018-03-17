from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import request, jsonify

app = Flask(__name__)

urls = [
{
	'id': 1,
	's_path': 'abc',
	'l_url': 'https://www.google.com'	
}
]


@app.route('/<string:url>')
def url_shorten(url):
	for single_url in urls:
		if url == single_url['s_path']:
			return redirect(single_url['l_url'])
	return 'request url doesnt exist'	
import time

@app.route('/home')
def home():
	return render_template('home.html')
	
@app.route('/add_url', methods=['POST'])
def add_url():
	if request.form['url']:			
		url_payload = {
			'id': len(urls) + 1,
		's_path': str(time.time())[0:5],
			'l_url': request.form['url']
		}
		urls.append(url_payload)	
	return jsonify(urls)
	
	
	
		
		

	
# run the server
if __name__ == '__main__':
	app.run(debug=True)