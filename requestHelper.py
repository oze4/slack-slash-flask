def request_body_to_string(request):
    try:
        return request.get_data().decode('utf8')
    except Exception as e:
        raise e
