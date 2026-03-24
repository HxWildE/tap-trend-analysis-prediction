import time

CURRENT_TIME = time.time()

def compute_velocity(post):
    age_hours = (CURRENT_TIME - post["created_utc"]) / 3600

    if age_hours == 0:
        age_hours = 1

    engagement = post["score"] + post["comments"]

    velocity = engagement / age_hours

    return velocity


def add_velocity(posts):
    for post in posts:
        post["velocity"] = compute_velocity(post)

    return posts