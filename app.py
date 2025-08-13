# add_numbers.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    # Validate
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Both a and b must be numbers"}), 400

    return jsonify({"sum": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
