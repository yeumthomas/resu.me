import urllib.request
from bs4 import BeautifulSoup


url = "https://www.monster.com/jobs/search/?q=python&where=Katy__2C-TX&intcid=skr_navigation_nhpso_searchMain"

with urllib.request.urlopen(url) as response:
   page = response.read()


jobs = []

soup = BeautifulSoup(page, 'html.parser')

for sec in soup.findAll('section', attrs = {'class': lambda x: x and x.startswith('card-content')}):

   # Job name
   name = sec.find('h2', attrs = {'class': 'title'})
   if name != None:
      name = name.find('a')
      if name != None:
         jobInfo = {'name': name.text[0:-2]}
         jobs.append(jobInfo)
         link = name['href']
         jobInfo['link'] = link
   
         with urllib.request.urlopen(link) as response:
            jobPage = response.read()
         newSoup = BeautifulSoup(jobPage, 'html.parser')
         
         # Job company & location
         fields = sec.findAll('span', attrs = {'class': 'name'})
         if fields[0] != None:
            jobInfo['company'] = fields[0].text
         else:
            jobInfo['company'] = fields[0]
         if fields[1] != None:
            jobInfo['location'] = fields[1].text[2:-2]
         else:
            jobInfo['location'] = fields[1]
   


   

