from flask import Flask, render_template
import random


app = Flask(__name__)



@app.route('/')
@app.route('/index/<title>')
def index(title):
    if 'инженер' in title:
        return render_template('base.html', title=title, img=1)
    elif 'строитель' in title:
        return render_template('base.html', title=title, img=2)
    else:
        return render_template('base.html', title=title, img=random.randint(1, 2))


if __name__ == '__main__':
    app.run('', 8080)
