from flask import Flask, session, render_template, request, redirect, url_for, flash, send_file
from flask.ext.script import Manager

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True,
))

manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph1')
def graph1():
    import matplotlib.pyplot
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    import random
    import string
    import os

    class TempImage(object):

        def __init__(self, file_name):
            self.file_name = file_name

        def create_png(self):
            fig, ax = matplotlib.pyplot.subplots()
            ax.set_title(u'IMINASHI GRAPH 2')
            x_ax = range(1, 284)
            y_ax = [x * random.randint(436, 875) for x in x_ax]
            ax.plot(x_ax, y_ax)

            canvas = FigureCanvasAgg(fig)
            canvas.print_figure(self.file_name)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            os.remove(self.file_name)

    chars = string.digits
    img_name = ''.join(random.choice(chars) for i in range(64)) + '.png'

    with TempImage(img_name) as img:
        img.create_png()
        return send_file(img_name, mimetype='image/png')

if __name__ == '__main__':
    manager.run()
