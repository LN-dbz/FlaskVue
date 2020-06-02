from ..api.test import ApiView, test
from ..api.main import main

all_view = [
    {
        'api': test,
        'endpoint': '/tests'
    },
    {
        'api': main,
        'endpoint': ''
    }
]

all_api = [
    {
        'api': ApiView,
        'endpoint': '/test'
    }
]
