
repository_url =  'TO BE DEFINED'

environments = {
    'dev': {
        'hosts': ['default'],
        'is_vagrant': True,
    },
    'qa': {
        'hosts': [],
        'superuser': 'root',
    },
    'prod': {
        'hosts': [],
        'superuser': 'root',
    },
}
