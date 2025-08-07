from flask import Flask
from app.generator import generate_traffic
from app.metrics import setup_metrics

app = Flask(__name__)
setup_metrics(app)

@app.route("/")
def index():
    return "Traffic Monitor API Running"

@app.route("/generate")
def generate():
    data = generate_traffic()
    return {"traffic_data": data}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)