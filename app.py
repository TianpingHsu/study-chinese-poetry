
from flask import Flask
from flask import request
import json
import tests.test

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test/hello/<string:name>")
def hello(name):
    return f"<p>Hello, {name}!</p>"

@app.route("/test/http", methods=['GET', 'POST'])
def http_test():
    if request.method == 'GET':
        return "<p>this is a GET method</p>"
    elif request.method == 'POST':
        return "<p>this is a POST method</p>"
    else:
        return f"<p>unsupported method: {request.method}</p>"


@app.route("/test/templates")
def templates_test():
    pass

# http://localhost:5000/test/protection/encrypt?key=secret&plaintext=I-love-you
@app.route("/test/protection/encrypt")
def test_protection_encrypt():
    k = request.args.get('key', '')
    p = request.args.get('plaintext', '')
    if k and p:
        t = tests.test.Test()
        c = t.encrypt_with_aes(k, p)
        return f"<p>key: {k}</p> <p>plainttext: {p}</p><p>query str: {request.query_string}</p><p>{c}</p><p>{t.decrypt_with_aes(k, c)}</p>"
        #pass
    else:
        return f"<p>bad url, sample input: '/test/protection/encrypt?key=secret&plaintext=hello-world'</p>"

@app.route('/test/poetry')
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

@app.route("/test/baginstrument", methods=['POST'])
def test_baginstrument():
    data = request.get_json()
    print(data)
    return "<p>this is a POST method</p>"



'''
@app.route("/test/upload-files/<filename>")
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('./sandbox/uploaded_file.txt')
'''


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

