import urllib.request
from bs4 import BeautifulSoup



def scrape_coursera(keyword):

    def format_coursera(keyword):
        """
        assumes keyword is a string of one or more words
        """
        if ' ' in keyword is False:
            return '?query=' + keyword + '&='
        else:
            keyword_list = keyword.split()
            url = '?query='
            for word in keyword_list:
                url += word + '%20'
            url = url[:-3] + "&="
            return url

    updated_keyword = format_coursera(keyword)

    url = "https://www.coursera.org/search" + updated_keyword

    with urllib.request.urlopen(url) as response:
        page = response.read()

    courses = []

    soup = BeautifulSoup(page, 'html.parser')
    for li in soup.findAll('li', attrs = {'class':'ais-InfiniteHits-item'}):

        # Course name
        name = li.find('h2', attrs = {'class':'color-primary-text card-title headline-1-text'})
        courseInfo = {'name': name.text}
        courses.append(courseInfo)

        # Course image
        img = li.find('img')
        courseInfo['img'] = img['src']
        
        # Course link
        tag = li.find('a', attrs = {'data-click-key':'search.search.click.search_card'})
        link = "https://www.coursera.org" + tag['href']
        courseInfo['link'] = link
        with urllib.request.urlopen(link) as response:
            coursePage = response.read()
        courseSoup = BeautifulSoup(coursePage, 'html.parser')

        # Course description
        desc = courseSoup.find('p', attrs = {'class': 'max-text-width m-b-0'})
        if desc != None:
            courseInfo['desc'] = desc.text
        else:
            courseInfo['desc'] = desc

        # Course rating 
        rating = courseSoup.find('span', attrs = {'class': '_16ni8zai m-b-0 rating-text number-rating number-rating-expertise'})
        if rating != None:
            courseInfo['rating'] = rating.text 
        else:
            courseInfo['rating'] = rating

        # Course fields
        allFields = []
        fields = courseSoup.findAll('div', attrs = {'class': lambda x: x and x.startswith('_16ni8zai m-b-0')})
        for field in fields:
            if field != None:
                allFields.append(field.text)
            else:
                allFields.append(" ")

        for field in allFields:
            if field != 0:
                if 'Level' in field:
                    courseInfo['level'] = field
                elif '%' in field:
                    courseInfo['onlinePercentage'] = field
        
        # Course primary language
        courseInfo['lang'] = allFields[len(allFields) - 1]

        # Course skills
        skills = []
        for skill in courseSoup.findAll('span', attrs = {'class': '_1q9sh65'}):
            skills.append(skill.text)
        courseInfo['skills'] = skills

        # Course provider
        provider = courseSoup.find('img', attrs = {'class': '_1g3eaodg'})
        if provider != None:
            courseInfo['provider'] = provider['alt']
        else:
            provider = courseSoup.find('div', attrs = {'class': lambda x: x and x.startswith('m-b-1s m-r-1')})
            if provider != None:
                courseInfo['provider'] = provider.text
            else:
                courseInfo['provider'] = provider

        # Course info
        info = courseSoup.find('div', attrs = {'class': ['m-t-1 m-b-3 description', 'm-t-1 description']})
        if info != None:
            courseInfo['info'] = info.text
        else:
            courseInfo['info'] = info

        # Course platform (Coursera)
        courseInfo['platform'] = 'Coursera'

    return courses


def scrape_udemy(keyword):
    def format_udemy(keyword):
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

    formatted_keyword = format_udemy(keyword)

    # example
    # NO WORK url = "https://www.udemy.com/courses/search/?price=price-free&q=cooking&sort=relevance"
    # NO WORK url = "https://www.codecademy.com/search?query=html"
    # WORKS url = "https://www.classcentral.com/search?q=python"
    # ? MAYBE url = https://www.udemy.com/courses/search/?price=price-free&q=" + formatted_keyword + "&sort=relevance"
    # WORKS url = 'https://www.monster.com/jobs/search/?q=cook&where=Katy__2C-TX&intcid=skr_navigation_nhpso_searchMain'
    url = 'https://www.simplyhired.com/search?q=cook&l=Houston%2C+TX&job=GVLzF1t5rkWSStUfDTAQJNP_O4M1qSA0W_NL9ZX8Z8lwhw2pg33n4w'
    with urllib.request.urlopen(url) as response:
        page = response.read()
    soup = BeautifulSoup(page, 'html.parser')


    return {"soup": str(soup)}
    #
    # for div in soup.findAll('div', attrs={'class': 'popover--popover--t3rNO popover--popover-hover--14ngr'}):
    #
    #     course_info = {}
    #
    #     # Course link
    #     tags = div.findAll('a', attrs={'class': 'udlite-custom-focus-visible course-card-link--link--3uQEZ'})
    #     for tag in tags:
    #         if tag['href']:
    #             link = "https://www.udemy.com" + tag['href']
    #     course_info['link'] = link
    #     print(link)
    #     # with urllib.request.urlopen(link) as response:
    #     #     coursePage = response.read()
    #     # courseSoup = BeautifulSoup(coursePage, 'html.parser')
    #
    #
    #
    #     # print(course_info)
    #     #
    #     # # Course name
    #     # name = div.find('h3', attrs={'class': 'name-heading'})
    #     #
    #     # print(name)
    #     # course_info['name'] = name.text
    #     #
    #     # print(course_info)
    #
    #     return course_info

    #     # Course link
    #     tag = li.find('a', attrs={'data-click-key': 'search.search.click.search_card'})
    #     link = "https://www.coursera.org" + tag['href']
    #     courseInfo['link'] = link
    #     with urllib.request.urlopen(link) as response:
    #         coursePage = response.read()
    #     courseSoup = BeautifulSoup(coursePage, 'html.parser')
    #
    #     # Course description
    #     desc = courseSoup.find('p', attrs={'class': 'max-text-width m-b-0'})
    #     if desc != None:
    #         courseInfo['desc'] = desc.text
    #     else:
    #         courseInfo['desc'] = desc
    #
    #     # Course rating
    #     rating = courseSoup.find('span',
    #                              attrs={'class': '_16ni8zai m-b-0 rating-text number-rating number-rating-expertise'})
    #     if rating != None:
    #         courseInfo['rating'] = rating.text
    #     else:
    #         courseInfo['rating'] = rating
    #
    #     # Course level
    #     level = courseSoup.find('div', attrs={'class': '_16ni8zai m-b-0'})
    #     if level != None:
    #         courseInfo['level'] = level.text
    #     else:
    #         courseInfo['level'] = level
    #
    #     # Course skills
    #     skills = []
    #     for skill in courseSoup.findAll('span', attrs={'class': '_1q9sh65'}):
    #         skills.append(skill.text)
    #     courseInfo['skills'] = skills
    #
    #     # Course primary language
    #     # lang = courseSoup.find('div', attrs = {'class': '_16ni8zai m-b-0'})
    #     # if lang != None:
    #     #     courseInfo[lang] = lang.text
    #     # else:
    #     #     courseInfo[lang] = lang
    #
    #     # # Course subtitle languages
    #     # subs = courseSoup.find
    # return courses

