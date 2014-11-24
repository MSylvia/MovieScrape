#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name: IMDBParser.py
# Purpose: Scrape latest movies off IMDB and get average age of the actors
#
# Author: Matthew Sylvia (msylvia@nukefile.net)
#
# Created: 11/22/2014
# Copyright: (c) 2014 Matthew Sylvia
# Licence: MIT
#-----------------------------------------------------------------------------

from Parser import *
from datetime import datetime, date


class IMDBParser(Parser):
    'Information about a Movie'

    # ---------------------------------------------------------
    def PostProcess_MovieID(self, list):
    # ---------------------------------------------------------
        data = []
        for item in list:
            data.append(item.attrib['href'].split('/')[3])
        return data

    # ---------------------------------------------------------
    def PostProcess_ActorName(self, list):
    # ---------------------------------------------------------
        data = []
        for item in list:
            data.append(item.find('span').text)
        return data

    # ---------------------------------------------------------
    def PostProcess_ActorID(self, list):
    # ---------------------------------------------------------
        data = []
        for item in list:
            data.append(item.attrib['href'].split('/')[2])
        return data

    # ---------------------------------------------------------
    def PostProcess_ActorBirthdate(self, list):
    # ---------------------------------------------------------
        data = []
        try:
            for item in list:
                raw = item.attrib['datetime']
                template = "%Y-%m-%d"
                age = self.Calculate_Age(datetime.strptime(raw, template))
                data.append(age)
        except:
            data.append(0)

        age = 0
        if len(data) != 0:
            age = data[0]
        return age

    # ---------------------------------------------------------
    def Calculate_Age(self, born):
    # ---------------------------------------------------------
        today = date.today()
        return today.year - born.year - (
            (today.month, today.day) < (born.month, born.day))

    # ---------------------------------------------------------
    def __init__(self):
    # ---------------------------------------------------------
        # Movie Title
        self.Add('movie_title',
                 'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha',
                 '//*[@class="title"]/a/text()')
        # Movie ID
        self.Add('movie_id',
                 'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha',
                 '//*[@class="title"]/a',
                 IMDBParser.PostProcess_MovieID)
        # Actor Name
        self.Add('actor_name',
                 'http://www.imdb.com/title/{0}/fullcredits',
                 '//*[@itemprop="actor"]/a',
                 IMDBParser.PostProcess_ActorName)
        # Actor ID
        self.Add('actor_id',
                 'http://www.imdb.com/title/{0}/fullcredits',
                 '//*[@itemprop="actor"]/a',
                 IMDBParser.PostProcess_ActorID)
        # Actor Age
        self.Add('actor_age',
                 'http://www.imdb.com/name/{0}/',
                 '//*[@id="name-born-info"]/time',
                 IMDBParser.PostProcess_ActorBirthdate)
    # ---------------------------------------------------------
        #print self.list
