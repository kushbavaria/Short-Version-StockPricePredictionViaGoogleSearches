from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
companyName = 'Apple' 
class Analysis:
	def __init__(self, term):
		self.term = term
		self.sentiment = 0
		self.subjectivity = 0
		self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)

	def run(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.text, 'html.parser')
		headline_results = soup.find_all('div', class_='kCrYT')
		for text in headline_results:
			blob = TextBlob(text.get_text())	
			self.sentiment += blob.sentiment.polarity / len(headline_results)
			self.subjectivity += blob.sentiment.subjectivity / len(headline_results)

company = Analysis(companyName)
company.run()
print("Overall sentiment was " + str(company.sentiment) + " on a scale from -1 to 1") 
print("Overall bias was " + str(company.subjectivity) + " on a scale from -1 to 1")   
