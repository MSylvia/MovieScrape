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
    # parser = MovieParser()
    # print parser.GetMovies('01606', 2)

    # # Print everyone
    # for movieid, movie in parser.moviesList.items():
    #     for actorid in movie.actorIDs:
    #         print parser.actorsList[actorid]

    parser = IMDBParser()
    parser.Add('movieTitles',
               'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha',
               ['01606'],
               '//*[@class="title"]/a/text()'
               )

    parser.Process('movieTitles')
    print parser.Get('movieTitles')

    parser.Add('movieIDs',
               'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha',
               ['01606'],
               '//*[@class="title"]/a',
               parser.PostProcessMovieTitle)

    parser.Process('movieIDs')
    print parser.Get('movieIDs')

    parser.Add('actorNames',
               'http://www.imdb.com/title/{0}/fullcredits',
               'tt0365907',
               '//*[@itemprop="actor"]/a',
               parser.PostProcessActorName)

    parser.Process('actorNames')
    print parser.Get('actorNames')


