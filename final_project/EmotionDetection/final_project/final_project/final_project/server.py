from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(**name**)

@app.route("/")
def index():
return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
text_to_analyze = request.args.get("textToAnalyze")

```
if not text_to_analyze:
    return "Invalid input! Please try again.", 400

result = emotion_detector(text_to_analyze)

response = (
    f"For the given statement, the system response is "
    f"'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, "
    f"'fear': {result['fear']}, "
    f"'joy': {result['joy']} and "
    f"'sadness': {result['sadness']}. "
    f"The dominant emotion is {result['dominant_emotion']}."
)

return response
```

if **name** == "**main**":
app.run(host="localhost", port=5000)
