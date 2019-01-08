from flask import Flask, request, jsonify
import service

app = Flask(__name__)

@app.route('/')
def index():
    return("App works!")


#  {"number": 5, "times": "2.4"}
@app.route('/multiply', methods=["POST"])
def multiply():
    if request.method == "POST":
        if ((isinstance(request.json["number"],int) or isinstance(request.json["number"],float)) and
                 (isinstance(request.json["times"],int) or isinstance(request.json["times"],float))):
            number = float(request.json["number"])
            times = float(request.json["times"])
            try:
                result = service.mul(number, times)
                return(jsonify({"number": result}))
            except:
                return(jsonify({"error": "values are too high for calculation"}), 400)
        else:
            return(jsonify({"error": "pass numbers, please"}), 400)
    else:
        return(jsonify({"error": "non-post method"}), 400)

#  {"words": ["word", "lord", "master", "keys", "foot", "loot"]}
@app.route('/group', methods=["POST"])
def group():
    if request.method == "POST":
        try:
            words = request.json["words"]
            for wrd in words:
                if not isinstance(wrd, str):
                    return(jsonify({"error": "pass words as string, please"}), 400)
            sorted_words = service.group_words(words)
            return(jsonify({"words": sorted_words}))
        except:
            return(jsonify({"error": "pass words, please"}), 400)
    else:
        return(jsonify({"error": "non-post method"}))

#  {"text": "hello -> brave -> new world"}
@app.route('/serialize', methods=["POST"])
def serialize():
    if request.method == "POST":
        try:
            text = request.json["text"]
        except:
            return(jsonify({"error": "pass text, please"}), 400)
        try:
            result = service.seri(text)
            return(jsonify({"text": result}))
        except:
            return(jsonify({"error": "conversion went wrong"}), 409)
    else:
        return(jsonify({"error": "non-post method"}))