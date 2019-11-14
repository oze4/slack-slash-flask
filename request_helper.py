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

            try:
                request_token = request.form["token"]
            except:
                return False

            #og_headers = dict(request.headers)
            headers = {
                "X-Slack-Signature": request.headers["X-Slack-Signature"],
                "X-Slack-Request-Timestamp": request.headers["X-Slack-Request-Timestamp"],
                "x-raw-body": request_string,
                "x-raw-token": request_token
            }

            return headers

            validated = fetch.post(SLACK_VALIDATOR_URL, headers=headers)

            try:
                return validated.json()
            except:
                return validated
            #return True

        except Exception as e:
            ex = exceptions.GetException()
            raise Exception(ex)
