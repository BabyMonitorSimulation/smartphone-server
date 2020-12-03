def construct_response(type, msg, to):
    return {
        'type': type,
        'msg': msg,
        'route': {
            'from': 'smp',
            'to': to,
        }
    }
