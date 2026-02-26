from flask import Flask, render_template
import os  # <-- needed for Render PORT

app = Flask(__name__)

@app.route("/")
def home():
    photos = [
        "photos/us.jpeg",
        "photos/photo1.jpeg",
        "photos/photo2.jpeg",
        "photos/photo3.jpeg"
    ]
    return render_template("index.html", photos=photos)

if __name__ == "__main__":
    # Use the port Render provides, default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)