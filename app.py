from flask import Flask, jsonify, request
import json, settings, os
import requestHelper


app = Flask(__name__)

@app.route("/slash/flask", methods=['GET', 'POST'])
def slash_flask():
    try:
        request_string = requestHelper.request_body_to_string(request)
        print(request_string)
        return "[Python:Flask]::Success :smile:"
    except:
        return "Error :cry:" + jsonify("nope")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT"))
