from django.test import TestCase

import requests

api = "https://opentdb.com/api.php?amount=20&difficulty=easy"
response = requests.get(api)
data = response.json()

# Now you can use the data from the API in your test cases