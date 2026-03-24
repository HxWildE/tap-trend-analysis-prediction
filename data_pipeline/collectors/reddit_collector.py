import requests
import time

HEADERS = {
    "User-Agent": "trend-intelligence-app/0.1"
 }
# Without agent reddit considers illegittimate bot
# and declines data / request

SUBREDDITS = ["technology", "india", "worldnews"]

BASE_URL = "https://www.reddit.com/r/{}/hot.json?limit=25"


def fetch_subreddit(subreddit):
    url = BASE_URL.format(subreddit)
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        # raise 404 if not found server
        data = response.json()

        posts = []

        for post in data["data"]["children"]:
            p = post["data"]

            posts.append({
                "subreddit": subreddit,
                "title": p["title"],
                "score": p["score"],
                "comments": p["num_comments"],
                "created_utc": p["created_utc"],
                "url": p["url"]
            })

        return posts

    except Exception as e:
        print(f"Error fetching {subreddit}: {e}")
        return []


def collect_all():

    all_posts = []

    for sub in SUBREDDITS:
        print(f"Fetching r/{sub}...")
        posts = fetch_subreddit(sub)
        all_posts.extend(posts)

        time.sleep(1)  # avoid rate limiting

    return all_posts


if __name__ == "__main__":
    data = collect_all()

    print(f"\nCollected {len(data)} posts\n")

    for post in data[:5]:
        print(post)