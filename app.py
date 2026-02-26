from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # List of photos to display in the gallery
    photos = [
        "photos/us.jpeg",
        "photos/photo1.jpeg",
        "photos/photo2.jpeg",
        "photos/photo3.jpeg"
    ]
    
    # Render the template with the photos only
    return render_template("index.html", photos=photos)

if __name__ == "__main__":
    app.run(debug=True)