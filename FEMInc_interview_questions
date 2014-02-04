import nltk
import ner
import re
import json
import os
import urllib2
from urllib import urlencode

from pprint import pprint

# open the contents
with open('CodeAssignmentDataSet.json') as json_file:
    json_data = json.load(json_file)
    json_file.close()
    pprint(json_data[0:4])
    
# The OMDB API's constant for searching movie titles
titleUrl = "http://www.omdbapi.com/?"   # i=&t=
 
# Fetches a movie from OMDB API as a Json object
# Note: expects a full title name
def fetchMovie(predicate):
    predicate = urlencode({'i': predicate, 't': predicate})
    request = urllib2.Request(titleUrl + predicate, None, {'user-agent':'whatever'})
    opener = urllib2.build_opener()
    stream = opener.open(request)
    return json.load(stream)
    
    
# search names of actors and movie/show titles from description and title
def name(sentence):
    r = re.compile('([A-Z]\w+(?=[\s\-][A-Z])(?:[\s\-][A-Z]\w+)+)', re.UNICODE)
    match = r.findall(sentence)
    #assert(match is not None)
    #extracted = match.group(0)
    return match #extracted
    
# take the union of two lists of dictionaries
def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))
    
name_from_title = name(json_data[2].get('title'))
name_from_description = name(json_data[2].get('description'))
names = union(name_from_title, name_from_description)
print names

# If a fanous movie or actor is confirmed, it will be updated into the orgininal data set
#
for item in json_data[0:4]:
    xx = {'FamousMovie': fetchMovie(names[0])['Title']}
    item.update(xx)
    
pprint (json_data[0:4])
