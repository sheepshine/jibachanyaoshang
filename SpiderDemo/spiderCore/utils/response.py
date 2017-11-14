from django.http import HttpResponse
import json


def response_fn_success(message):
    return HttpResponse(json.dumps({"message": message, "code": "0"}), content_type="application/json")


def response_fn_error(message):
    return HttpResponse(json.dumps({"message": message, "code": "100001"}), content_type="application/json")
