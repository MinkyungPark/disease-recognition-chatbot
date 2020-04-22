from flask import Flask, render_template, request
from predict import get_category

app = Flask(__name__)

@app.route('/')
def chat():
	return render_template('main.html')


@app.route('/user/<name>')
def chatUser(name):
	return render_template('main.html', name=name)


@app.route('/get')
def getResponse():
    userText = request.args.get('msg')
    return '제가 생각한 증상은 ' + get_category(userText) + '입니다.'


if __name__ == '__main__':
	app.run(debug=False, threaded=False)
