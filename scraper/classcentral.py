import urllib.request
from bs4 import BeautifulSoup

def scrape_other(keyword):
    """
    courses
        - name DONE
        - image DONE
        - hyperlink to platform
        - description
        - rating <-- sorted by DONE
        - language
        - institution/sponsor DONE
        - platform name
    :param keyword:
    :return:
    """
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

    updated_keyword = format_other(keyword)

    # url = "https://www.classcentral.com/search?q=" + updated_keyword
    url = "https://www.classcentral.com/search?q=python"

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

        # get sponsor
        sponsor = tr.a.text
        course_info['sponsor'] = sponsor

        # get name
        name = tr.span.text
        course_info['name'] = name

        # get rating
        rating = tr.find('td', class_='hide-on-hover fill-space relative')['data-timestamp']
        course_info['rating'] = ("{:.1f}".format(float(rating)))

        # link to platform class
        class_link = "https://www.classcentral.com" + tr.find('a', class_='color-charcoal block line-tight course-name')['href']

        with urllib.request.urlopen(class_link) as response:
            coursePage = response.read()
        courseSoup = BeautifulSoup(coursePage, 'html.parser')



        # get image
        img = courseSoup.img['src'] #find('img', class_="block absolute top left width-100 height-100")
        course_info['img'] = img

        # get course description





        courses.append(course_info)
    return courses


        # Check if its an Ad

        # tr[data-lookup-course-]
        #
        # td = tr.find('td', attrs={'class': "width-12-16 large-up-width-8-16 xxlarge-up-width-9-16 relative"})
        # # if td_two['data-track-click'] == "ad_click": # or if data=track-click is in td_two.keys()
        # #     continue
        #

    #     # find
    #     sponsor = td_two.find('div', attrs={'class': 'truncate'}).find('a', attrs={'class': 'color-charcoal small-down-text-2 text-3'}).text
    #     course_info['sponsor'] = sponsor
    #
    #     courses.append(course_info)
    # return courses

    #     # Course name
    #     name = li.find('h2', attrs={'class': 'color-primary-text card-title headline-1-text'})
    #     courseInfo = {'name': name.text}
    #     courses.append(courseInfo)
    #
    #     # Course image
    #     img = li.find('img')
    #     courseInfo['img'] = img['src']
    #
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
    #     # Course fields
    #     allFields = []
    #     fields = courseSoup.findAll('div', attrs={'class': lambda x: x and x.startswith('_16ni8zai m-b-0')})
    #     for field in fields:
    #         if field != None:
    #             allFields.append(field.text)
    #         else:
    #             allFields.append(" ")
    #
    #     for field in allFields:
    #         if field != 0:
    #             if 'Level' in field:
    #                 courseInfo['level'] = field
    #             elif '%' in field:
    #                 courseInfo['onlinePercentage'] = field
    #
    #     # Course primary language
    #     courseInfo['lang'] = allFields[len(allFields) - 1]
    #
    #     # Course skills
    #     skills = []
    #     for skill in courseSoup.findAll('span', attrs={'class': '_1q9sh65'}):
    #         skills.append(skill.text)
    #     courseInfo['skills'] = skills
    #
    # return courses