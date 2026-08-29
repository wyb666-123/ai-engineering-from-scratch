from flask import Flask, request, jsonify
import platform

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="ai-dev-cpu flask API is alive!", python=platform.python_version())

@app.get("/predict")
def predict():
    n = request.args.get("n", type=float)
    if n is None:
        return jsonify(error="missing query param ?n=<number>"), 400
    return jsonify(input=n, output=n ** 2, model="toy-square-v1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

