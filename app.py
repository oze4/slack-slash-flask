from flask import Flask, request, Response
import json, env_settings, os
import request_helper


app = Flask(__name__)

HOST = "0.0.0.0"
PORT = os.getenv("PORT")
DEBUG = True


@app.route("/slash/flask", methods=['POST'])
def slash_flask():
    try:
        validated = request_helper.validate_request(request)
        return validated
        if validated == True:
            return "[Python:Flask]::Success :smile: "
        else:
            return Response('<Unable to validate request>', 401, {'x-no-validation':'validation="unable"'})
    except Exception as e:
        print("***ERROR***")
        print(e)
        print("***ERROR***")
        return "Error :cry: "


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)

