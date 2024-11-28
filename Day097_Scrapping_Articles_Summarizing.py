import os
import requests
import openai
from bs4 import BeautifulSoup

url = input("Pastr wiki URL: ")

openai.organisation = os.environ["organisationID"]
openai.api_key = os.environ["openai"]
openai.Model.list()

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "parser.html")
article = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
                      
text = ""
for articles in article:
    content = article.find_all("p")
    for p in content:
        text += p.text

prompt = f"Summarise the text below in no more than 3 paragraphs. {text}"
response = openai.Completion.create(model="text-davinci-002", prompt = prompt, temperature=0, max_tokens=150)

refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
    print(ref.text.replace("^ ", ""))

print(response["choises"][0]["text"].strip())



