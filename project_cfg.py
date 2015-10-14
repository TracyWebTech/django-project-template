
defaults = {
    'repository': 'TO BE DEFINED',
    'superuser': 'root',
}

environments = {
    'dev': {
        'hosts': ['default'],
        'is_vagrant': True,
    },
    'prod': {
        'hosts': [],
    },
}
