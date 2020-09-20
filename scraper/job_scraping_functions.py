import urllib.request
from bs4 import BeautifulSoup


def scrape_monster(skill, location):
    def format_skill(keyword):
        """
        assumes keyword is a string of one or more words
        """
        if ' ' in keyword is False:
            return keyword
        else:
            keyword_list = keyword.split()
            url = ''
            for word in keyword_list:
                url += word + '-'
        url = url[:-1]
        return url

    def format_location(location):
        place_list = location.split(", ")
        for ind in range(len(place_list)):
            place_list[ind] = place_list[ind].replace(' ', '-')
        return place_list

    formatted_skill = format_skill(skill)
    place_list = format_location(location)

    url = "https://www.monster.com/jobs/search/?q=" + formatted_skill + '&where=' + place_list[0] + "__2C--" + place_list[1]

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

                jobs.append(jobInfo)

    return jobs


def scrape_simplyhired(skill, location):
    def format_skill(keyword):
        """
        assumes keyword is a string of one or more words
        """
        if ' ' in keyword is False:
            return keyword
        else:
            keyword_list = keyword.split()
            url = ''
            for word in keyword_list:
                url += word + '+'
        url = url[:-1]
        return url

    def format_location(location):
        place_list = location.split(", ")
        for ind in range(len(place_list)):
            place_list[ind] = place_list[ind].replace(' ', '+')
        return place_list

    formatted_skill = format_skill(skill)
    place_list = format_location(location)
    url = "https://www.simplyhired.com/search?q=" + formatted_skill + "&l=" + place_list[0] + "%2C+" + place_list[1]

    with urllib.request.urlopen(url) as response:
        page = response.read()

    jobs = []
    soup = BeautifulSoup(page, 'html.parser')

    for div in soup.findAll('div', attrs = {'class': lambda x: x and x.startswith('SerpJob-jobCard')}):
        # Job name
        name = div.find('a', attrs={'rel':'nofollow'})
        if name != None:
            jobInfo = {'name': name.text}
            jobs.append(jobInfo)
            link = 'https://www.simplyhired.com/' + name['href']
            jobInfo['link'] = link

        # Job company
            company = div.find('span', attrs={'JobPosting-labelWithIcon jobposting-company'})
            if company != None:
                jobInfo['company'] = company.text
            else:
                jobInfo['company'] = company

        # Job location
            location = div.find('span', attrs={'JobPosting-labelWithIcon jobposting-location'})
            if company != None:
                jobInfo['location'] = location.text[0:-1]
            else:
                jobInfo['location'] = location

            jobs.append(jobInfo)

    return jobs

   

