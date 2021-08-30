import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://coreyms.com/')

soup = BeautifulSoup(source.text, 'lxml')

# print(soup.prettify())

f = open('scrape.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Headline', 'Summary', 'Video'])

articles = soup.find_all('article')

for article in articles:

	headline = article.h2.text

	print(headline)

	summary = article.find('div', class_='entry-content').p.text

	print(summary)

	try:
		video = article.find('iframe', class_='youtube-player')['src']

		video = video.split('/')[4].split('?')[0]

		video = f'https://www.youtube.com/watch?v={video}'
		
	except Exception as e:
		video = None

	print(video)

	print()

	writer.writerow([headline, summary, video])

f.close()

