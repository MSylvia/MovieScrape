#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name: Actor.py
# Purpose: Scrape latest movies off IMDB and get average age of the actors
#
# Author: Matthew Sylvia (msylvia@nukefile.net)
#
# Created: 11/22/2014
# Copyright: (c) 2014 Matthew Sylvia
# Licence: MIT
#-----------------------------------------------------------------------------


class Actor:
    'Information about an Actor'

    name = ''
    ID = ''
    movieIDs = []
    age = 0

    # ---------------------------------------------------------
    def __init__(self, name, ID, movieIDs, age=0):
    # ---------------------------------------------------------
        self.name = name
        self.ID = ID
        self.movieIDs = movieIDs
        self.age = age

    # ---------------------------------------------------------
    def __str__(self):
    # ---------------------------------------------------------
        template = 'Name="{0}", ID="{1}" MovieIDs={2} Age={3}'
        return template.format(self.name.encode('utf-8'),
                               self.ID,
                               self.movieIDs,
                               self.age)
