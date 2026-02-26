from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    photos = [
        "photos/us.jpeg",
        "photos/photo1.jpeg",
        "photos/photo3.jpeg",
        "photos/photo2.jpeg",
    ]
    return render_template("index.html", photos=photos)

if __name__ == "__main__":
    app.run(debug=True)