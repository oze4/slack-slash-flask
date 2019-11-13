import json, os
import requests as fetch


SLACK_VALIDATOR_URL = os.getenv("SLACK_VALIDATOR_URL")


def validate_request(request):
    if SLACK_VALIDATOR_URL == "":
        return False
    else:
        try:
            request_data = request.get_data()
            request_string = request_data.decode('utf8')
            request_as_json = json.loads(request_string)

            try:
                request_token = request_as_json["token"]
            except:
                return False

            headers = {
                "x-raw-body": request_string,
                "x-raw-token": request_token
            }
            validated = fetch.post(SLACK_VALIDATOR_URL, headers=headers)
            return validated
            #return True
        except:
            return False
