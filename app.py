from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/api/paraphrase", methods=['POST'])
def paraphrase():
    data = request.get_json()

    inputText = data.get("text")
    print(type(inputText))
    print(inputText)

    return jsonify({"output": "none"}), 200

