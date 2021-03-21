# Audio speech recogniser

Audio speech recogniser is a [flask](https://flask.palletsprojects.com/en/1.1.x/) based app that transcribes audio. It uses a web interface to request an 
audio file. The audio file is then transcribed using the Google speech recognition API via the 
[Speech Recognition](https://pypi.org/project/SpeechRecognition/) package.

The transcribed text is then displayed to the user. The app currently only accepts audio files in 
the [wav](https://en.wikipedia.org/wiki/WAV) format.

I also use the [Dosis](https://fonts.google.com/specimen/Dosis) font from the Google [fonts](https://fonts.google.com/) service.

Improvements:
- [ ] Add support for non-English languages 
- [ ] Display speech statistics e.g. most common words, etc
