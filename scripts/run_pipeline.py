from data_pipeline.collectors.reddit_collector import collect_all
from ml_engine.pipelines.full_pipeline import run_pipeline


if __name__ == "__main__":
    print("Collecting data...")
    raw_posts = collect_all()

    print("Running ML pipeline...")
    results = run_pipeline(raw_posts)

    print("\n🔥 TOP TRENDING POSTS:\n")

    for post in results[:10]:
        print(f"{post['text']}")
        print(f"Velocity: {post['velocity']:.2f}")
        print("-" * 50)