from flask import Flask, render_template, url_for
from forms import registrationform, loginform

app = Flask(__name__)

app.config['SECRET_KEY'] = '01686c55b426db5e7e04277274cd1033'

posts = [
    {
        'author': 'Steven Clive',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'dateposted': 'April 20, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'dateposted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', authpost=posts, title='Blog Homepage')

@app.route('/about')
def about():
    return render_template('about.html', title='Blog About Page')

@app.route('/register')
def register():
    form = registrationform()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = registrationform()
    return render_template('register.html', title='Register', form=form)

if __name__ == "__main__":
    app.run(debug=True)