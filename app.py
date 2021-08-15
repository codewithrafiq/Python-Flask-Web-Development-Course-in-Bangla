from flask import Flask,render_template

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


@app.route("/home")
@app.route("/")
def home():
    return render_template('index.html',data=datas)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/python")
def pythonCode():
    return render_template("python.html")


if __name__ == "__main__":
    app.run(debug=True)