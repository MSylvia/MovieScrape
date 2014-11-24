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

import sys
import time
from MovieParser import *
from IMDBParser import *


def siginthndlr(sig, frame):
    sys.exit(0)
    print "Keyboard interrupt catched"

# ---------------------------------------------------------
if __name__ == "__main__":
# ---------------------------------------------------------
    for arg in sys.argv:
        print arg

    parser = MovieParser(IMDBParser())

    print '{:<13}'.format('ID'),'{:<9}'.format('Average'),'{:<70}'.format('Title')
    start_time = time.time()
    movies = parser.GetMovies(sys.argv[1])
    for movie in movies:
        parser.SetAges(movie.ID)
        print '{:<13}'.format(movie.ID),'{:<9}'.format(movie.average),'{:<70}'.format(movie.name)

    print time.time() - start_time, "seconds"

    # parser = MovieParser(IMDBParser())
    # print '{:<13}'.format('ID'),'{:<9}'.format('Average'),'{:<70}'.format('Title')
    # # ---------------------------------------------------------
    # start_time = time.time()
    # parser.CreateMovie('A Walk Among the Tombstones', 'tt0365907') # Cheating for time test
    # parser.SetAges('tt0365907')
    # # ---------------------------------------------------------
    # movie = parser.GetMovie('tt0365907')
    # print '{:<13}'.format(movie.ID),'{:<9}'.format(movie.average),'{:<70}'.format(movie.name)
    # print time.time() - start_time, "seconds"
