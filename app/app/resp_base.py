from django.http import HttpResponse
from http import HTTPStatus
import json

def response_ok(data: any, meta: any = None, headers={'Content-Type': 'application/json'}, *args, **kwargs):
    return HttpResponse(json.dumps({
        'success': True,
        'data': data,
        'meta': meta
    }), status=HTTPStatus.OK, headers=headers, *args, **kwargs)

def response_err(code='ERROR', message='ERROR', status=HTTPStatus.BAD_REQUEST, headers={}):
    return HttpResponse(json.dumps({
        'Code': code,
        'Message': message
    }), status=status, headers=headers)

def response_cr(data: any, headers={'Content-Type': 'application/json'}, *args, **kwargs):
    return HttpResponse(json.dumps({
        'success': True,
        'data': data,
    }), status=HTTPStatus.CREATED, headers=headers, *args, **kwargs)

def response_val(errors):
    return HttpResponse(json.dumps({
        'Code': 'validation_error',
        'Message': 'Validation Error',
        'Errors': errors
    }), status=HTTPStatus.BAD_REQUEST)