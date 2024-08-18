
from flask import Flask
from flask import request

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

'''
@app.route("/test/upload-files/<filename>")
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('./sandbox/uploaded_file.txt')
'''


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

