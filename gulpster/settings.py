config = dict(
    rabbitmq={
        'username': 'guest',
        'password': 'guest',
        'host': '0.0.0.0:8024',
        'virtual_host': '/',
        'queue': 'test',
        'exchange': 'message',
        'exchange_type': 'direct',
        'routing_key': 'example.test',
    },
)
