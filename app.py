from flask import Flask, jsonify, request
import json, settings, os


app = Flask(__name__)

@app.route("/slash/flask", methods=['GET', 'POST'])
def slash_flask():
    try:
        print(request.get_data())
        return "[Python:Flask]::Success :smile:"
    except:
        return "Error :cry:" + jsonify("nope")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT"))
