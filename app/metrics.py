from flask import Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

traffic_volume = Gauge("traffic_volume", "Number of vehicles")
average_speed = Gauge("average_speed", "Average vehicle speed")
accident_count = Gauge("accident_count", "Accidents reported")

def setup_metrics(app):
    @app.route("/metrics")
    def metrics():
        traffic_volume.set(132)
        average_speed.set(65.4)
        accident_count.set(2)
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)