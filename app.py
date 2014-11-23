#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name: app.py
# Purpose: Scrape latest movies off IMDB and get average age of the actors
#
# Author: Matthew Sylvia (msylvia@nukefile.net)
#
# Created: 11/22/2014
# Copyright: (c) 2014 Matthew Sylvia
# Licence: MIT
#-----------------------------------------------------------------------------

from MovieParser import *
from IMDBParser import *

if __name__ == "__main__":

    parser = MovieParser(IMDBParser())
    print parser.GetMovies('01606', 1)


    # parser = IMDBParser()
    # parser.Run('movie_title', ['01606'])
    # parser.Run('movie_title', ['01606'])
    # print parser.Get('movie_title')

    #-----------------------------
    # parser.Add('movieNames',
    #            'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha',
    #            ['01606'],
    #            '//*[@class="title"]/a/text()'
    #            )
    # parser.Process('movieNames')
    # print parser.Get('movieNames')

    # #-----------------------------
    # parser.Add('movieIDs',
    #            'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha',
    #            ['01606'],
    #            '//*[@class="title"]/a',
    #            parser.PostProcessMovieTitle)
    # parser.Process('movieIDs')
    # print parser.Get('movieIDs')

    # #-----------------------------
    # parser.Add('actorNames',
    #            'http://www.imdb.com/title/{0}/fullcredits',
    #            'tt0365907',
    #            '//*[@itemprop="actor"]/a',
    #            parser.PostProcessActorName)
    # parser.Process('actorNames')
    # print parser.Get('actorNames')

    # #-----------------------------
    # parser.Add('actorIDs',
    #            'http://www.imdb.com/title/{0}/fullcredits',
    #            'tt0365907',
    #            '//*[@itemprop="actor"]/a',
    #            parser.PostProcessActorID)
    # parser.Process('actorIDs')
    # actorIDS = parser.Get('actorIDs')

    # for x in actorIDS:
    #     parser.Add('actorAge',
    #                'http://www.imdb.com/name/{0}/',
    #                x,
    #                '//*[@id="name-born-info"]/time',
    #                parser.PostProcessActorBirthday)
    #     parser.Process('actorAge')
    #     print parser.Get('actorAge')
