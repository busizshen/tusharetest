from flask import Flask
from pythonwebTest.flaskT.ruweb2 import simple_page

app = Flask(__name__,static_folder="static")
app.register_blueprint(simple_page)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/page/<page>')
def hello_world1(page):
    print(page)
    return app.send_static_file(page)

if __name__ == '__main__':
    app.run(port = 1234)