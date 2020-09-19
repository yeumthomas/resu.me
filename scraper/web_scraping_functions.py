import urllib.request
from bs4 import BeautifulSoup

def format_keyword(keyword):
    """
    assumes keyword is a string of one or more words
    """
    if ' ' in keyword == False:
        return '?query=' + keyword + '&='
    else:
        keyword_list = keyword.split()
        url = '?query='
        for word in keyword_list:
            url += word + '%20'
        url = url[:-3] + "&="
        return url


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
        link = "https://www.coursera.org" + tag['href']
        courseInfo['link'] = link
        with urllib.request.urlopen(link) as response:
            coursePage = response.read()
        courseSoup = BeautifulSoup(coursePage, 'html.parser')

        # Course description
        desc = courseSoup.find('p', attrs={'class': 'max-text-width m-b-0'})
        if desc != None:
            courseInfo['desc'] = desc.text
        else:
            courseInfo['desc'] = desc

        # Course rating
        rating = courseSoup.find('span',
                                 attrs={'class': '_16ni8zai m-b-0 rating-text number-rating number-rating-expertise'})
        if rating != None:
            courseInfo['rating'] = rating.text
        else:
            courseInfo['rating'] = rating

        # Course level
        level = courseSoup.find('div', attrs={'class': '_16ni8zai m-b-0'})
        if level != None:
            courseInfo['level'] = level.text
        else:
            courseInfo['level'] = level

        # Course skills
        skills = []
        for skill in courseSoup.findAll('span', attrs={'class': '_1q9sh65'}):
            skills.append(skill.text)
        courseInfo['skills'] = skills

        # Course primary language
        # lang = courseSoup.find('div', attrs = {'class': '_16ni8zai m-b-0'})
        # if lang != None:
        #     courseInfo[lang] = lang.text
        # else:
        #     courseInfo[lang] = lang

        # # Course subtitle languages
        # subs = courseSoup.find
    return courses