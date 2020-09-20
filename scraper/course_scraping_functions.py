import urllib.request
from bs4 import BeautifulSoup


def scrape_coursera(keyword, q):
    """
    returns a list of objects where each is a course with the following keys:
        - name
        - img
        - link
        - desc
        - rating
        - lang
        - provider
        - platform
    """

    print('started coursera')

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

        # for field in allFields:
        #     if field != 0:
        #         if 'Level' in field:
        #             courseInfo['level'] = field
        #         elif '%' in field:
        #             courseInfo['onlinePercentage'] = field
        
        # Course primary language
        courseInfo['lang'] = allFields[len(allFields) - 1]

        # Course skills
        # skills = []
        # for skill in courseSoup.findAll('span', attrs = {'class': '_1q9sh65'}):
        #     skills.append(skill.text)
        # courseInfo['skills'] = skills

        # Course provider
        provider = courseSoup.find('img', attrs = {'class': '_1g3eaodg'})
        if provider != None:
            courseInfo['provider'] = provider['alt']
        else:
            provider = courseSoup.find('div', attrs={'class': lambda x: x and x.startswith('m-b-1s m-r-1')})
            if provider != None:
                courseInfo['provider'] = provider.text
            else:
                courseInfo['provider'] = provider

        # Course info
        info = courseSoup.find('div', attrs={'class': ['m-t-1 m-b-3 description', 'm-t-1 description']})
        if info != None:
            courseInfo['info'] = info.text
        else:
            courseInfo['info'] = info

        # Course platform (Coursera)
        courseInfo['platform'] = 'Coursera'

    print('finish coursera')
    q.put(courses)
    return courses


def scrape_other(keyword, q):
    """
    returns a list of objects where each is a course with the following keys:
        - name
        - img
        - link
        - desc
        - rating
        - lang
        - provider
        - platform
    """
    print('started other')

    def format_other(keyword):
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

    def remove_extra(str):
        """
        removes unnecessary newlines in string
        """
        return str.replace("\n", "").replace(" \n", "").replace("\n ", "")

    updated_keyword = format_other(keyword)

    url = "https://www.classcentral.com/search?q=" + updated_keyword

    with urllib.request.urlopen(url) as response:
        page = response.read()

    courses = []
    count = 0
    soup = BeautifulSoup(page, 'html.parser')
    # return str(soup.findAll('td', attrs={'class': 'width-12-16 large-up-width-8-16 xxlarge-up-width-9-16 relative'}))
    for tr in soup.findAll('tr', attrs={'class': 'row nowrap vert-align-middle padding-vert-small border-bottom border-gray-light'}):
        if count >= 10:
            break
        count += 1

        course_info = {}

        # get provider
        provider = tr.a.text
        course_info['provider'] = remove_extra(provider)

        # get name
        name = tr.span.text
        course_info['name'] = remove_extra(name)

        # get rating
        rating = tr.find('td', class_='hide-on-hover fill-space relative')['data-timestamp']
        course_info['rating'] = ("{:.1f}".format(float(rating)))

        # get platform
        platform = tr.find('a', class_='color-charcoal italic').text
        course_info['platform'] = remove_extra(platform)

        # link to platform class
        class_link = "https://www.classcentral.com" + tr.find('a', class_='color-charcoal block line-tight course-name')['href']

        with urllib.request.urlopen(class_link) as response:
            coursePage = response.read()
        courseSoup = BeautifulSoup(coursePage, 'html.parser')

        final_link = courseSoup.find("a", class_="margin-bottom-small btn-blue btn-medium width-100")['href']
        course_info['link'] = final_link

        # get image
        img = courseSoup.img['src'] #find('img', class_="block absolute top left width-100 height-100")
        course_info['img'] = img

        # get course description
        desc = courseSoup.find('div', class_="wysiwyg text-1 line-wide")
        if desc is None:
            desc = courseSoup.find('div', class_="truncatable-area is-truncated wysiwyg text-1 line-wide").text
        else:
            desc = desc.text
        course_info['desc'] = remove_extra(desc)

        # get language
        for anchor in courseSoup.aside.findAll('a', class_="text-2 color-charcoal margin-left-small line-tight"):
            if "English" in anchor.text or "Spanish" in anchor.text or "Italian" in anchor.text or "French" in \
                    anchor.text or "Mandarin" in anchor.text or "Korean" in anchor.text:
                course_info['lang'] = remove_extra(anchor.text)


        courses.append(course_info)
    
    print('finish other')
    q.put(courses)
    return courses