import flask
from flask_cors import CORS, cross_origin
import course_scraping_functions as course_scraping_func
import job_scraping_functions as job_scraping_func
import json
import multiprocessing

app = flask.Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["DEBUG"] = True


@app.route('/api/v1/scrapeCourses', methods=['POST'])
@cross_origin()
def scrape_courses():
    keyword = flask.request.form['keyword']
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=course_scraping_func.scrape_coursera, args=(keyword,q))
    p2 = multiprocessing.Process(target=course_scraping_func.scrape_other, args=(keyword,q))
    p1.start()
    p2.start()

    coursera = q.get()
    other = q.get()

    p1.join()
    p2.join()

    return json.dumps({
        'coursera': coursera,
        'other': other
    })

@app.route('/api/v1/scrapeJobs', methods=['POST'])
@cross_origin()
def scrape_jobs():
    keyword = flask.request.form['keyword']
    location = flask.request.form['location']

    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=job_scraping_func.scrape_monster, args=(keyword, location, q))
    p2 = multiprocessing.Process(target=job_scraping_func.scrape_simplyhired, args=(keyword, location, q))
    p1.start()
    p2.start()

    monster = q.get()
    simplyhired = q.get()

    p1.join()
    p2.join()

    return json.dumps({
        'monster': monster,
        'simplyhired': simplyhired
    })



app.run(host='0.0.0.0', port=3001, debug=True)