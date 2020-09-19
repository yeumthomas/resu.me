import urllib.request
from bs4 import BeautifulSoup

def format_keyword(keyword):
    """
    assumes keyword is a string of one or more words
    """

    if ' ' in keyword == False:
        return '?query=' + keyword + '&='
    else:
        keyword_list =



def scrape_coursera(keyword):

    format_keyword(keyword)

    url = "https://www.coursera.org/search?query=python&"

    with urllib.request.urlopen(url) as response:
        page = response.read()

    courses = []

    soup = BeautifulSoup(page, 'html.parser')
    for li in soup.findAll('li', attrs={'class': 'ais-InfiniteHits-item'}):
        # Course name
        name = li.find('h2', attrs={'class': 'color-primary-text card-title headline-1-text'})
        courseInfo = {'name': name.text}
        courses.append(courseInfo)

        # Course link
        tag = li.find('a', attrs={'data-click-key': 'search.search.click.search_card'})
        link = "https://www.coursera.org/" + tag['href']
        courseInfo['link'] = link
        with urllib.request.urlopen(link) as response:
            coursePage = response.read()
        courseSoup = BeautifulSoup(coursePage, 'html.parser')

        # Course description
        desc = courseSoup.find('p', attrs={'class': 'max-text-width m-b-0'})
        courseInfo['desc'] = desc

        print(courseInfo)