import flask
import course_scraping_functions as course_scraping_func
import json
import classcentral

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/scrape', methods=['POST'])
def scrape():
    # access payload

    keyword = flask.request.form['keyword']

    return json.dumps({'other': classcentral.scrape_other(keyword)})


    # # scrape coursera (returns as list of dicts)
    # coursera = course_scraping_func.scrape_coursera(keyword)
    #
    # response = {}
    #
    # # results are in json format
    # #return flask.jsonify.results
    # return json.dumps({'coursera': coursera})


app.run(host='0.0.0.0', port=3000, debug=True)