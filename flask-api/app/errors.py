from flask import jsonify


def user_not_present(user: str):
    return jsonify(
        {
            'data': {
                'success': 'False',
                'errors': {
                    'reason': 'forbidden',
                    'message': f'User {user} not present; Forbidden request'
                },
                'code': 403,
                'message': f'User {user} not present; Forbidden request'
            }
        }
    )


def user_present(user: str):
    return jsonify(
        {
            'data': {
                'success': 'False',
                'errors': {
                    'reason': 'forbidden',
                    'message': f'User {user} already present; Forbidden request'
                },
                'code': 403,
                'message': f'User {user} already present; Forbidden request'
            }
        }
    )


def family_present(family: str):
    return jsonify(
        {
            'data': {
                'success': 'False',
                'errors': {
                    'reason': 'forbidden',
                    'message': f'Family {family} already present; Forbidden request'
                },
                'code': 403,
                'message': f'Family {family} already present; Forbidden request'
            }
        }
    )


def invalid_format(param: str):
    return jsonify(
        {
            'data': {
                'success': 'False',
                'errors': {
                    'reason': 'invalid',
                    'message': f'Missing parameters {param}; Invalid request'
                },
                'code': 403,
                'message': f'Missing parameters {param}; Invalid request'
            }
        }
    )


def invalid_http_method(method: str, intended: str):
    return jsonify(
        {
            'data': {
                'success': 'False',
                'errors': {
                    'reason': 'forbidden',
                    'message': f'Made invalid HTTP method call {method} when it should be {intended}; Forbidden call'
                },
                'code': 403,
                'message': f'Made invalid HTTP method call {method} when it should be {intended}; Forbidden call'
            }
        }
    )
