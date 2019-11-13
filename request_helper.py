import json, os
import requests as fetch
import exceptions


SLACK_VALIDATOR_URL = os.getenv("SLACK_VALIDATOR_URL")


def validate_request(request):
    if SLACK_VALIDATOR_URL == "":
        return False
    else:
        try:
            request_data = request.get_data()
            request_string = request_data.decode('utf8')
            return request_string
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
        except Exception as e:
            ex = exceptions.GetException()
            raise Exception(ex)
            #raise Exception("error from request_helper " + str(e))
