from flask import Flask, render_template, request, redirect
import speech_recognition as sr

# setup basic app
app = Flask(__name__)

# route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("Form data received")

        # refresh the webpage if no valid file was submitted
        if "File" not in request.files:
            print("No valid file")
            return redirect(request.url)

        # handle empty transcribe request
        file = request.files["File"]
        if file.filename == "":
            print("Empty file")
            return redirect(request.url)

        # assumption file exists
        if file:
            print("valid file uploaded")
            recogniser = sr.Recognizer()

            # open audio in manageable format
            audioFile = sr.AudioFile(file)

            # read audio data
            with audioFile as source:
                data = recogniser.record(source)

            # parse the text from audio
            transcript = recogniser.recognize_google(data, key=None)
            print(transcript)

    return render_template("index.html", transcript=transcript)

if __name__ == "__main__":
    # debug=True for automatic refresh of app on save
    # threaded=True for handling multiple requests
    app.run(debug=True, threaded=True)