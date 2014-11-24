#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name: pool.py
# Purpose: Scrape latest movies off IMDB and get average age of the actors
#
# Author: Matthew Sylvia (msylvia@nukefile.net)
#
# Created: 11/23/2014
# Copyright: (c) 2014 Matthew Sylvia
# Licence: MIT
#-----------------------------------------------------------------------------

import sys
import time
import requests
from multiprocessing import Pool
from datetime import datetime, date
from lxml import html

# Movie ID
movie_id_template = 'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha'
movie_id_xpath = '//*[@class="title"]/a'
# Movie Name
movie_name_template = movie_id_template
movie_name_xpath = '//*[@class="title"]/a/text()'
# Actor ID
actor_id_template = 'http://www.imdb.com/title/{0}/fullcredits'
actor_id_xpath = '//*[@itemprop="actor"]/a'
# Actor Name
actor_name_template = actor_id_template
actor_name_xpath = '//*[@itemprop="actor"]/a'
# Actor Age
actor_age_template = 'http://www.imdb.com/name/{0}/'
actor_age_xpath = '//*[@id="name-born-info"]/time'


# ---------------------------------------------------------
def PostProcess_MovieID(list):
# ---------------------------------------------------------
    data = []
    for item in list:
        data.append(item.attrib['href'].split('/')[3])
    return data


# ---------------------------------------------------------
def PostProcess_ActorName(list):
# ---------------------------------------------------------
    data = []
    for item in list:
        data.append(item.find('span').text)
    return data


# ---------------------------------------------------------
def PostProcess_ActorID(list):
# ---------------------------------------------------------
    data = []
    for item in list:
        data.append(item.attrib['href'].split('/')[2])
    return data


# ---------------------------------------------------------
def PostProcess_ActorBirthdate(list):
# ---------------------------------------------------------
    data = []
    # Try and get age
    try:
        for item in list:
            raw = item.attrib['datetime']
            template = "%Y-%m-%d"
            age = Calculate_Age(datetime.strptime(raw, template))
            data.append(age)
    # If age is not formatted correctly or empty set to 0
    except:
        data.append(0)

    age = 0
    if len(data) != 0:
        age = data[0]
    return age


# ---------------------------------------------------------
def Calculate_Age(born):
# ---------------------------------------------------------
    today = date.today()
    return today.year - born.year - (
        (today.month, today.day) < (born.month, born.day))


# ---------------------------------------------------------
def Run(vars):
# ---------------------------------------------------------
    var = vars['var']
    template = vars['template']

    data = vars['data']

    finalData = {}

    for request in data:
        key = request['key']
        xpath = request['xpath']
        callback = None
        if 'callback' in request:
            callback = request['callback']

        # Make Request
        page = requests.get(template.format(var))
        tree = html.fromstring(page.text)

        # Parse
        rawValues = tree.xpath(xpath)

        if callback is not None:
            finalData[key] = callback(rawValues)
        else:
            finalData[key] = rawValues

    print 'DONE', var
    return finalData


# ---------------------------------------------------------
def BuildRequestActor(id):
# ---------------------------------------------------------
    return {'var': id,
            'template': actor_id_template,
            'data': [
                {
                    'key': 'name',
                    'xpath': actor_name_xpath,
                    'callback': PostProcess_ActorName
                },
                {
                    'key': 'id',
                    'xpath': actor_id_xpath,
                    'callback': PostProcess_ActorID
                },
            ]}


# ---------------------------------------------------------
def BuildRequestActorAge(id):
# ---------------------------------------------------------
    return {'var': id,
            'template': actor_age_template,
            'data': [
                {
                    'key': 'age',
                    'xpath': actor_age_xpath,
                    'callback': PostProcess_ActorBirthdate
                },
            ]}


# ---------------------------------------------------------
def BuildRequestMovie(id):
# ---------------------------------------------------------
    return {'var': id,
            'template': movie_id_template,
            'data': [
                {
                    'key': 'name',
                    'xpath': movie_name_xpath
                },
                {
                    'key': 'id',
                    'xpath': movie_id_xpath,
                    'callback': PostProcess_MovieID
                },
            ]}

# ---------------------------------------------------------
if __name__ == '__main__':
# ---------------------------------------------------------
    if len(sys.argv) < 2:
        print 'Error: Zipcode required'
        print 'Usage: python', sys.argv[0], '01606'
        sys.exit(0)

    for arg in sys.argv:
        print arg
    # -----------------------------------------------------

    # This should probably be lower, since I got blocked :(
    pool = Pool(processes=20)
    start_time = time.time()

    # Get Movies
    # -----------------------------------------------------
    data_movies = Run(BuildRequestMovie(sys.argv[1]))

    # Build actor request from the movie id's
    # -----------------------------------------------------
    request_actor = map(BuildRequestActor, data_movies['id'])
    #print request
    #print data_movies['id']

    # Run actor request in the pool
    # -----------------------------------------------------
    data_actor = pool.map(Run, request_actor)
    #print data_actor

    actor_ids = sum(
        list(data_actor[x]['id'] for x in xrange(0, len(data_actor))), [])
    actor_names = sum(
        list(data_actor[x]['name'] for x in xrange(0, len(data_actor))), [])
    #print actor_ids

    #dup_ids = [x for x in actor_ids if actor_ids.count(x) > 1]
    #dup_names = [x for x in actor_names if actor_names.count(x) > 1]

    # Build age request from the actor id's
    # -----------------------------------------------------
    request_age = map(BuildRequestActorAge, actor_ids)

    # Run actor request in the pool
    # -----------------------------------------------------
    data_age = pool.map(Run, request_age)

    actor_ages = sum(
        list(data_age[x]['age'] for x in xrange(0, len(data_age))), [])

    print actor_ages

    print time.time() - start_time, "seconds"
