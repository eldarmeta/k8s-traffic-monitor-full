import random

def generate_traffic():
    return {
        "vehicles": random.randint(50, 200),
        "avg_speed": round(random.uniform(30.0, 100.0), 2),
        "accidents": random.randint(0, 5)
    }