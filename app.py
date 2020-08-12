#-*- coding:utf-8 -*-
from flask import Flask, render_template, request, json, make_response
from predict import get_category

app = Flask(__name__)

@app.route('/')
def chat(): 
	msg = request.args.get('msg',"없음")
	return render_template('main.html', msg=msg)


@app.route('/get')
def getResponse():
	jpype.attachThreadToJVM()
	msg = request.args.get('msg')
    return '제가 생각한 증상은 ' + get_category(msg) + '입니다.'

	
@app.route('/req')
def getAnswer():
	jpype.attachThreadToJVM()

	msg = request.args.get('msg')
	res = get_category(msg)
	dic = {"answer": res}
	result = json.dumps(dic, ensure_ascii=False)
	return result


@app.route('/user/<name>')
def chatUser(name):
	return render_template('main.html', name=name)


if __name__ == '__main__':
	app.run(debug=False, threaded=False)

