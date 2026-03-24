from ml_engine.preprocessing.cleaner import clean_posts
from ml_engine.trend_detection.velocity import add_velocity

def run_pipeline(raw_posts):
    # Step 1: Clean
    cleaned = clean_posts(raw_posts)

    # Step 2: Add velocity
    with_velocity = add_velocity(cleaned)

    # Step 3: Sort by trend strength
    sorted_posts = sorted(
        with_velocity,
        key=lambda x: x["velocity"],
        reverse=True
    )

    return sorted_posts