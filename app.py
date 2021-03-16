from flask import Flask, render_template

# setup basic app
app = Flask(__name__)

 # route for homepage
@app.route("/", methods=["GEt"])
def index():
    return "hello world"

if __name__ == "__main__":
    # debug= rue for automatic refresh of app on save
    # threaded=True for handling multiple requests
    app.run(debug=True, threaded=True)