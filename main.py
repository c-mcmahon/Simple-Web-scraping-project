import bs4
import requests
import pickle


#---------- Getting the HTML link -------------
html = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

#------------- Creating a soup object from the HTML --------
soup = bs4.BeautifulSoup(html.text,features="html.parser")

#-------- Scanning through HTML file to find the part were interested in ------
table = soup.find('table',{'class':'wikitable sortable'})
tickers = []
#------- Finding the rows in the table -----------
rows = table.findAll('tr')[1:]
#------ Iterating over rows to add ticker to ticker list -------
for row in rows:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker[:-1])


#------Saving ticker list to pickle file ------------
with open('snp500.pickle','wb') as file:
    pickle.dump(tickers,file)

#-------- Opening pickle file to save time ----------
with open('snp500.pickle','rb') as file:
    tickers = pickle.load(file)


print(tickers)

