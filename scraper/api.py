import flask
import course_scraping_functions as course_scraping_func
import job_scraping_functions as job_scraping_func
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/scrape-courses', methods=['POST'])
def scrape_courses():
    keyword = flask.request.form['keyword']

    return json.dumps({
        'coursera': course_scraping_func.scrape_coursera(keyword),
        'other': course_scraping_func.scrape_other(keyword)
    })

@app.route('/api/v1/scrape-jobs', methods=['POST'])
def scrape_jobs():
    keyword = flask.request.form['keyword']
    location = flask.request.form['location']

    return json.dumps({
        'monster': job_scraping_func.scrape_monster(keyword, location),
        'simplyhired': job_scraping_func.scrape_simplyhired(keyword, location)
    })



app.run(host='0.0.0.0', port=3001, debug=True)