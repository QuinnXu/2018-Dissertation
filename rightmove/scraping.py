from bs4 import BeautifulSoup
import requests
import json
import re

# scraping data according to property id
id = 64952815
def scrape(id):
    id = str(id)
    url = 'https://www.rightmove.co.uk/student-accommodation/property-'+id+'.html'
    html = requests.get(url).text

    # loading in beautifualsoup
    soup = BeautifulSoup(html,features='html5lib')
    result = soup.find('script', text=re.compile("RIGHTMOVE.ANALYTICS.PageViewTracker.trackOnClick"))
    data = result.get_text()
    data = data.split('{')[4]
    data = data.split(',')[:-5]

    dict={
        'id':id
    }

    for i in data:
        i = i.replace('"','').split(':')
        dict[i[0]]=i[1]

    return dict