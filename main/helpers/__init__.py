__author__ = 'Gungor'
import urllib
import re
import json
from StringIO import StringIO

base_url = 'http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&q='

class RateMyProf:
    def __init__(self, first_name, last_name):
        helper_url = '+AND+schoolid_s%3A742&defType=edismax&qf=teacherfullname_t^1000+autosuggest&bf=pow%28total_number_of_ratings_i%2C2.1%29&sort=total_number_of_ratings_i+desc&siteName=rmp&rows=20&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+averagehelpfulscore_rf+averageclarityscore_rf+averageeasyscore_rf+schoolid_s'

        self.url = base_url + first_name + "+" + last_name + helper_url


    def crawlURL(self, addedURL):
        url = addedURL
        json = urllib.urlopen(url).read()
        return json

    def get_data(self):
        data = self.crawlURL(self.url)
        io = StringIO(data)
        json_data = json.load(io)
        self.name = json_data['response']['docs'][0]['teacherfirstname_t']
        self.last_name = json_data['response']['docs'][0]['teacherlastname_t']
        self.average_rating = json_data['response']['docs'][0]['averageratingscore_rf']

        self.helpful = json_data['response']['docs'][0]['averagehelpfulscore_rf']
        self.clarity = json_data['response']['docs'][0]['averageclarityscore_rf']
        self.easy = json_data['response']['docs'][0]['averageeasyscore_rf']
