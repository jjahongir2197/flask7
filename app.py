from flask import Flask, render_template

app = Flask(__name__)

user = {
    "name": "Jahongir",
    "age": 17,
    "job": "Python Developer"
}

@app.route("/")
def profile():
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
