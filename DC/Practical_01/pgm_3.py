import googleapiclient.discovery
import pandas as pd

API_KEY = "AIzaSyDcE1eApJwqRxyUUaGwaJb0Qm8uM72a8bs"

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

query = "artificial intelligence"
max_results = 10

request = youtube.search().list(
    part="snippet",
    q=query,
    type="video",
    maxResults=max_results,
    order="relevance"
)
response = request.execute()

records = []

for item in response.get("items", []):
    video_id = item["id"]["videoId"]
    snippet = item["snippet"]
    
    stats_request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    stats_response = stats_request.execute()
    stats = stats_response["items"][0]["statistics"] if stats_response["items"] else {}
    
    records.append({
        "video_id": video_id,
        "title": snippet["title"],
        "description": snippet["description"],
        "published_at": snippet["publishedAt"],
        "channel_title": snippet["channelTitle"],
        "views": int(stats.get("viewCount", 0)),
        "likes": int(stats.get("likeCount", 0)),
        "comments": int(stats.get("commentCount", 0))
    })

df = pd.DataFrame(records)
df.to_csv("youtube_videos.csv", index=False)
print(f"Saved {len(records)} videos to youtube_videos.csv")