import re
from flask import Flask,render_template,request,redirect
import random

from werkzeug.utils import redirect

app = Flask(__name__)


datas =[
    {
        "id":1,
        "title":"Test Todo 1",
    },
        {
        "id":2,
        "title":"Test Todo 2",
    },
        {
        "id":3,
        "title":"Test Todo 3",
    },
        {
        "id":4,
        "title":"Test Todo 4",
    },
]


@app.route("/home",methods=["GET","POST"])
@app.route("/")
def home():
    if request.method == "POST":
        title = request.form["title"]
        print("title------>",title)
        new_todo={
            "id" : random.randint(1,99999999999),
            "title" : title,
        }
        datas.append(new_todo)
    return render_template('index.html',data=datas)

@app.route("/remove/<int:todoid>")
def removeTodo(todoid):
    for todo in datas:
        if todo["id"]==todoid:
            datas.remove(todo)
    return redirect('/')

@app.route("/update/<int:todoid>")
def updateTodo(todoid):
    for todo in datas:
        if todo["id"]==todoid:
            return render_template('update.html',todo=todo)
    return redirect('/')

@app.route("/updatetodo",methods=["POST"])
def update():
    title = request.form['title']
    id = request.form['todoid']
    # print("title------>",title)
    # print("id------>",id)
    for todo in datas:
        if todo["id"]==int(id):
            todo["title"]=title
            return redirect('/')
    return "ERROR"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/python")
def pythonCode():
    return render_template("python.html")

if __name__ == "__main__":
    app.run(debug=True)