
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
import json
import tests.test

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return app.send_static_file('index.html')

@app.route("/test/hello/<string:name>")
def hello(name):
    return f"<p>Hello, {name}!</p>"

# http://localhost:5000/test/protection/encrypt?key=secret&plaintext=I-love-you
@app.route("/cmd/protection/encrypt")
def test_protection_encrypt():
    k = request.args.get('key', '')
    p = request.args.get('plaintext', '')
    if k and p:
        t = tests.test.Test()
        c = t.encrypt_with_aes(k, p)
        return f"<p>key: {k}</p> <p>plainttext: {p}</p><p>query str: {request.query_string}</p><p>{c}</p><p>{t.decrypt_with_aes(k, c)}</p>"
    else:
        return f"<p>bad url, sample input: '/test/protection/encrypt?key=secret&plaintext=hello-world'</p>"

@app.route('/cmd/poetry')
def test_poetry():
    chuci_path = './chinese-poetry/楚辞/chuci.json'
    f = open(chuci_path)
    chuci = json.load(f)
    ret = ''
    for item in chuci:
        title = item['title']
        author = item['author']
        content = '<br>'.join(item['content'])
        ret += f'<p>{title}</p><p>{author}</p><p>{content}</p>'
        ret += '<p><br></p>'
    return ret

@app.route("/test/http", methods=['GET', 'POST'])
def http_test():
    # print("\nRequest Details:")
    # print(f"Method: {request.method}")
    # print(f"Path: {request.path}")
    # print(f"Headers:\n {request.headers}")
    # print(f"Form Data: {request.form}")
    # print(f"Query Parameters: {request.args}")
    # print(f"JSON Data: {request.json}")
    # print(f"Files: {request.files}")
    if request.method == 'GET':
        return "<p>this is a GET method</p>"
    elif request.method == 'POST':
        if request.form:
            return render_template('test-http.html', data=json.dumps(request.form.to_dict()))
        elif request.json:
            return render_template('test-http.html', data=json.dumps(request.get_json()))
        else:
            return "<p>this is a POST method</p>"
        
    else:
        return f"<p>unsupported method: {request.method}</p>"

@app.route('/static/<static_file>')
def test_bochk(static_file):
        return app.send_static_file(static_file + '.html')

@app.route('/templates/<template_file>')
def test_template(template_file):
    return render_template(template_file + '.html')

@app.route('/templates/hello/<name>')
def test_template_hello(name):
    return render_template('hello.html', person=name)

@app.route('/')
def index():
    return render_template('index.html', action=url_for('http_test'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

