#!/usr/bin/python

from MovieParser import *

if __name__ == "__main__":
    parser = MovieParser()
    print parser.GetMovies('01606', 2)

    # print actorsList[moviesList['tt0365907'].actorIDs[0]]
    # print len(actorsList), len(moviesList)
    # print moviesList['tt0365907'].actorIDs

    # Print everyone
    for movieid, movie in parser.moviesList.items():
        for actorid in movie.actorIDs:
            print parser.actorsList[actorid]
