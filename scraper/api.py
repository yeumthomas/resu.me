import flask
import web_scraping_functions as scraping_func
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/scrape', methods=['POST'])
def scrape():
    # access payload

    keyword = flask.request.form['keyword']

    # scrape coursera (returns as list of dicts)
    coursera = scraping_func.scrape_coursera(keyword)


    print(coursera)
    response = {}

    # results are in json format
    #return flask.jsonify.results
    return json.dumps({'coursera': coursera})


app.run(host='0.0.0.0', port=3000, debug=True)