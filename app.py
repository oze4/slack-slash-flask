from flask import Flask, request, Response
import json, env_settings, os, dotenv
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
        #return validated
        if type(validated) is bool:
            if validated == True:
                return "[Python:Flask]::Success :smile: "
            else:
                return Response('<Unable to validate request>', 401, {'x-no-validation':'validation="unable"'})
        else:
            return validated.json()
    except Exception as e:
        print("***ERROR***")
        print(e)
        print("***ERROR***")
        return "Error :cry: " + e


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)

