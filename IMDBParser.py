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


class IMDBParser(Parser):
    'Information about a Movie'

    # =========================================================
    def PostProcessMovieTitle(self, list):
        data = []
        for item in list:
            data.append(item.attrib['href'].split('/')[3])
        return data

    # =========================================================
    def PostProcessActorName(self, list):
        data = []
        for item in list:
            data.append(item.find('span').text)
        return data
