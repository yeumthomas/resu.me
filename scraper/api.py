import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/scrape', methods=['POST'])
def scrape():

    def scrape_coursera():
        return "coursera"
    # access payload
    # keyword = flask.request.form['keyword']

    # scrape coursera





    # results are in json format
    #return flask.jsonify.results
    return {"haha": "ahhahhaha"}


app.run(host='0.0.0.0', port=3000, debug=True)