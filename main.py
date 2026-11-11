import requests
from send_email import send_email

topic = "bangladesh"
api_key = "890603a55bfa47048e4490069ebee18c"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=890603a55bfa47048e4490069ebee18c&"
       "language=en")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
# ⚡ Bolt Optimization: Use list comprehension and ''.join() instead of += for O(n) string building
# Impact: Prevents memory reallocation overhead, creating a faster and more memory-efficient string build
articles_content = [
    article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n\n"
    for article in content.get("articles", [])[:20]
    if article.get("title") is not None and article.get("description") is not None
]
body_content = "".join(articles_content)

message = f"""Subject: Today's News

{body_content}"""
message = message.encode("utf-8")
send_email(message=message)
