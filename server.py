from flask import Flask, render_template
#### Hold down shift when refrreshing browser for a hrad reload of all css files

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")  #change to warren.html to see cv


if __name__ == "__main__":
    app.run(debug=True)