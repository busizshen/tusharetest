from flask import Flask
from testflask.flaskT.ruweb2 import simple_page
import pygal
from math import cos
def drawSvg():
    xy_chart = pygal.XY()
    xy_chart.title = 'XY Cosinus'
    xy_chart.add('x = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
    xy_chart.add('y = cos(x)', [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)])
    xy_chart.add('x = 1', [(1, -5), (1, 5)])
    xy_chart.add('x = -1', [(-1, -5), (-1, 5)])
    xy_chart.add('y = 1', [(-5, 1), (5, 1)])
    xy_chart.add('y = -1', [(-5, -1), (5, -1)])
    xy_chart.render_to_file('./static/bar_chart.svg')

app = Flask(__name__,static_folder="static")
app.register_blueprint(simple_page)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hello')
def hello_world2():
    print(123)
    drawSvg()
    return app.send_static_file("hello.html")

@app.route('/page/<page>')
def hello_world1(page):
    print(123)
    drawSvg()
    return app.send_static_file(page)

if __name__ == '__main__':
    # drawSvg()
    app.run(port = 1234)

