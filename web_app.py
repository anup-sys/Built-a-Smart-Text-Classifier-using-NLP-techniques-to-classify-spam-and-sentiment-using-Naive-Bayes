from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['message']
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    
    result = "Spam" if pred == 1 else "Not Spam"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)