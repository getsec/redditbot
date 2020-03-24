import praw
import requests
import shutil

def download_image(url ,title):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(f"static/{title}.jpg", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f) 

secret = "1M9LuTEHCPzucVWbE8KY0Y6aXgI"
app_id = "J01TWV-gcgcCKQ"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

reddit = praw.Reddit(client_id=app_id ,
                     client_secret=secret, 
                     user_agent=UA)



image_urls = []
image_titles = []

subreddit_list = [
    "ProgrammerHumor",
    "funny",
    "dankmemes",
    "comics",
    "wholesomememes",
    "BlackPeopleTwitter"
]

for subreddit in subreddit_list:
    sr = reddit.subreddit(subreddit) 
    posts = sr.hot(limit=150)
    for post in posts:
        url = post.url
        title = post.title.rstrip("'").replace("/", ".").rstrip("'").replace(' ', '_').replace('.','-').replace('?','')
        print(title)
        print(url)
        download_image(url ,f"{subreddit}__{title}")
        
