from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    # Accept either "a" and "b" OR "num1" and "num2"
    a = data.get("a", data.get("num1"))
    b = data.get("b", data.get("num2"))

    # Validate
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Both a and b must be numbers"}), 400

    return jsonify({"sum": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
