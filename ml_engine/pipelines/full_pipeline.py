from ml_engine.preprocessing.cleaner import clean_posts
from ml_engine.trend_detection.velocity import add_velocity
from ml_engine.trend_detection.acceleration import add_acceleration


def run_pipeline(raw_posts):
    # Step 1: Clean
    cleaned = clean_posts(raw_posts)

    # Step 2: Velocity
    with_velocity = add_velocity(cleaned)

    # Step 3: Acceleration
    with_acceleration = add_acceleration(with_velocity)

    # Step 4: Final Score
    for post in with_acceleration:
        post["final_score"] = post["velocity"] + post["acceleration"]

    # Step 5: Sort
    sorted_posts = sorted(
        with_acceleration,
        key=lambda x: x["final_score"],
        reverse=True
    )

    return sorted_posts