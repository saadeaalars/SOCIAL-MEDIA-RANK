from flask import Flask, request, render_template
from modules.toxic_checker import check_toxicity # Detoxify फाइल इम्पोर्ट करें

app = Flask(_name_)

@app.route("/")
def index():
    return render_template("index.html")    

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["text"] # HTML फॉर्म से टेक्स्ट लो
result = check_toxicity(text) # Detoxify से एनालिसिस करो

# रिजल्ट को HTML पेज में भेजो
return render_template("index.html", text=text, result=result)

if _name_ == "_main_":
app.run(debug=True)