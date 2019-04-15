from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
from flask_cors import CORS, cross_origin
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)
@app.route("/getText", methods=['POST','GET'])
def getText():

    if request.method == 'POST':
        jsonData = request.get_json(force=True)
        textDescription = jsonData['textDescription']

        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(textDescription)
        #print("{:-<65} {}".format(textDescription, str(vs)))

        userRequired = {
            'type': 'sentiment',
            'sentiment':str(vs),
            'status': 1
        }
        return jsonify(userRequired)
        sys.exit()

if __name__ == '__main__':
    app.debug = True
    app.run(host = '192.168.43.173',port=5005)