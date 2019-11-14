from flask import Flask, request, Response
import json
import os
import dotenv
import request_helper

dotenv.load_dotenv(verbose=True)

HOST = "0.0.0.0"
PORT = os.getenv("PORT")
DEBUG = True
SUCCESS_RESPONSE = "[Python][Flask]  :tada:  Success!  :tada:"
ERROR_RESPONSE = "[Python][Flask]  :cry:  ERROR  :cry:"

app = Flask(__name__)


@app.route("/slash/flask", methods=['POST'])
def slash_flask():
    try:
        validated = request_helper.validate_request(request)
        if validated == True:
            return SUCCESS_RESPONSE
        return ERROR_RESPONSE
    except:
        return ERROR_RESPONSE


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
