def compute_acceleration(post):
    score = post["score"]
    comments = post["comments"]
    velocity = post["velocity"]

    # avoid division issues
    if score == 0:
        score = 1

    discussion_ratio = comments / score

    acceleration = velocity * discussion_ratio

    return acceleration


def add_acceleration(posts):
    for post in posts:
        post["acceleration"] = compute_acceleration(post)

    return posts