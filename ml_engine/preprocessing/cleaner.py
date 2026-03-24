import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)   # remove links
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # remove symbols
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_posts(posts):
    cleaned = []

    for post in posts:
        cleaned.append({
            "subreddit": post["subreddit"],
            "text": clean_text(post["title"]),
            "score": post["score"],
            "comments": post["comments"],
            "created_utc": post["created_utc"]
        })

    return cleaned