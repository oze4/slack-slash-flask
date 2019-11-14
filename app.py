from flask import Flask, request, Response
import json
import os
import dotenv
import request_helper

dotenv.load_dotenv(verbose=True)

HOST = "0.0.0.0"
PORT = os.getenv("PORT")
DEBUG = True

app = Flask(__name__)


@app.route("/slash/flask", methods=['POST'])
def slash_flask():
    try:
        validated = request_helper.validate_request(request)
        if validated == True:
            return "[Python][Flask] :tada: Success! :tada: "
        return "[Python][Flask] :cry: ERROR :cry: "
    except Exception as e:
        return "Error :cry: " + str(e)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
