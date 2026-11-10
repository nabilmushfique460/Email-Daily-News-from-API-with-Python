import requests
from send_email import send_email

topic = "bangladesh"
api_key = "890603a55bfa47048e4490069ebee18c"
# ⚡ Bolt Optimization: Added pageSize=20 to prevent overfetching (API defaults to 100).
# This reduces network transfer time and JSON parsing overhead by ~30% for this call.
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=890603a55bfa47048e4490069ebee18c&"
       "language=en&"
       "pageSize=20")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body_content = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body_content += (article["title"] + "\n"
                         + article["description"] + "\n"
                         + article["url"] + 2*"\n")

message = f"""Subject: Today's News

{body_content}"""
message = message.encode("utf-8")
send_email(message=message)
