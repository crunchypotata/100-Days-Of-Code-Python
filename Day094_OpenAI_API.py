import os
import requests
import json
import openai

news = os.environ["news"]
openai.organisation = os.environ["organisationID"]
openai.api_key = os.environ["openai"]
openai.Model.list()

country = "gb"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey{news}"

result = requests.get(url)
data = result.json()
# print(json.dumps(data, intent=2))
counter = 0 
for article in data["articles"]:
    counter +=1 
    if counter >5:
        break
    prompt = (f"""Summarise{article["url"]} in one sentence""")
    response = openai.Completition.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=20)
    print(response["choises"][0]["text"].strip())
    time.sleep(20) #fix error