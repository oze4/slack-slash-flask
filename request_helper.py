import json
import os
import requests as fetch


try:
    SLACK_VALIDATOR_URL = os.getenv("SLACK_VALIDATOR_URL")
except:
    SLACK_VALIDATOR_URL = ""


def validate_request(request) -> bool:
    # If an env variable was not supplied for a validation URL return false
    if SLACK_VALIDATOR_URL == "":
        return False
    try:
        # Get request body - Flask makes you run this get_data() method which
        # initializes request data so you can then read it. 
        request_string = request.get_data().decode('utf8')

        # Since Slack sends us request as 'application/x-www-form-urlencoded' we have
        # to grab data from our request using '.form'.
        # We attempt to grab the 'token' from the Slack request - if it does not
        # exist, we know it's not a valid request so we return false.
        try:
            request_token = request.form["token"]
        except:
            return False

        # Slack needs the following headers in order to perform validation.
        # We grab required headers from our request, and append 'x-raw-body' and
        # 'x-raw-token' since our validator service requires those headers.
        # Header 'x-raw-body' contains the raw body from our original request.
        # Header 'x-raw-token' contains the token (as a string) from our original request.
        headers = {
            "X-Slack-Signature": request.headers["X-Slack-Signature"],
            "X-Slack-Request-Timestamp": request.headers["X-Slack-Request-Timestamp"],
            "x-raw-body": request_string,
            "x-raw-token": request_token
        }

        # Send the request we just crafted to our validator service, so that it
        # can check if we received a valid request or not.
        validated = fetch.post(SLACK_VALIDATOR_URL, headers=headers)

        # Try to convert the validator response to JSON.
        # The validator service returns a JSON object formatted like '{ "status": true }'
        # or '{ "status": false }'.
        try:
            validated_json = validated.json()
            status = validated_json["status"]
            if status == True or status == "true":
                return True
            return False
        except:
            return False
    # Catch any exceptions we receive
    except:
        return False
