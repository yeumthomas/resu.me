import flask
import course_scraping_functions as course_scraping_func
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/scrape', methods=['POST'])
def scrape():
    # access payload

    keyword = flask.request.form['keyword']

    return json.dumps({
        'coursera': course_scraping_func.scrape_coursera(keyword),
        'other': course_scraping_func.scrape_other(keyword)
    })

app.run(host='0.0.0.0', port=3000, debug=True)