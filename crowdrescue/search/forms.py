from django import forms
from django.utils import timezone
import requests
import json


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

    def search(self):
        # TODO add hook to run the actual search
        # tweets = requests.get("http://www.example.com")  # will be replaced by twitterbot API address
        # response = json.loads(tweets)  # used if we need to deserialize the response
        # return response --> this will send the dictionary over to the template

        return [{
            "date": timezone.now(),
            "handle": "@someone",
            "text": "random test text",
            "link": "http://example.com",
        }]
