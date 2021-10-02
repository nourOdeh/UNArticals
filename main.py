import requests, json
from bs4 import BeautifulSoup

json_array = []

for page_number in range(10):
  print('parsing page: ' + str(page_number))
  url = 'https://news.un.org/en/news/region/middle-east?page=' + str(page_number)
  request = requests.get(url)
  soup = BeautifulSoup(request.text, 'html.parser')
  parent_div_soup = soup.find("div", { 'class': 'view-listing-pages-solr'})
  views = parent_div_soup.find_all('div', { 'class': 'views-row' })

  for view in views:
    json_row = {}
    json_row['story_title'] = view.find("h1", { 'class': 'story-title' }).text
    json_row['story_body'] = view.find("div", { 'class': 'news-body' }).text
    json_row['story_url'] = "https://news.un.org" + view.find("h1", { 'class': 'story-title' }).find("a").get('href')
    json_array.append(json_row)

print(len(json_array))
with open('result.json', 'w') as output_file:
  json.dump(json_array, output_file)