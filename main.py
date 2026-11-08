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
body_content_list = []
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        # ⚡ Bolt: Optimizing string concatenation using list append and f-strings
        # instead of the += operator which creates new strings in each iteration
        body_content_list.append(f"{article['title']}\n{article['description']}\n{article['url']}\n\n")

body_content = "".join(body_content_list)

message = f"""Subject: Today's News

{body_content}"""
message = message.encode("utf-8")
send_email(message=message)
