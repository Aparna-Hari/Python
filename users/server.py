from flask import Flask, render_template, redirect, request, session
from models.user_model import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def show_all():
    users = User.get_all()
    return render_template("read.html", users=users)


@app.route('/create_user')
def create():
    return render_template("create.html")


@app.route('/new_user', methods = ["POST"])
def new_user():
    User.save(request.form)
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug = True)

