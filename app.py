from flask import Flask, render_template, request

# setup basic app
app = Flask(__name__)

 # route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("Form data received")
    return render_template("index.html")

if __name__ == "__main__":
    # debug= rue for automatic refresh of app on save
    # threaded=True for handling multiple requests
    app.run(debug=True, threaded=True)