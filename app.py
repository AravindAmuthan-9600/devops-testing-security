from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Security Demo</title>
        </head>
        <body>
            <h1>DevOps Testing & Security Demo</h1>
            <p>Application is running successfully.</p>
        </body>
    </html>
    """


@app.route("/api/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is healthy"
    })


@app.route("/api/add")
def add():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    if a is None or b is None:
        return jsonify({
            "error": "a and b are required"
        }), 400

    return jsonify({
        "result": a + b
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
