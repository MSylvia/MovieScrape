#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name: MovieParser.py
# Purpose: Scrape latest movies off IMDB and get average age of the actors
#
# Author: Matthew Sylvia (msylvia@nukefile.net)
#
# Created: 11/22/2014
# Copyright: (c) 2014 Matthew Sylvia
# Licence: MIT
#-----------------------------------------------------------------------------

from Movie import *
from Actor import *


class MovieParser:
    'Get movies by zipcode. Can limit number of movies returned.'

    actorsList = {}
    moviesList = {}
    zipcodeList = {}

    parser = None

    # ---------------------------------------------------------
    def __init__(self, parser):
    # ---------------------------------------------------------
        self.parser = parser

    # Based on Data
    #=============================
    # ---------------------------------------------------------
    def GetMovies(self, zipcode):
    # ---------------------------------------------------------
        self.CreateMovies(zipcode)
        return [self.moviesList[x] for x in self.zipcodeList[zipcode]]

    # ---------------------------------------------------------
    def GetMovie(self, movieID):
    # ---------------------------------------------------------
        return self.moviesList[movieID]

    # ---------------------------------------------------------
    def CreateMovies(self, zipcode):
    # ---------------------------------------------------------
        zipcode = zipcode.encode('utf-8')

        if zipcode in self.zipcodeList:
            return
            # result = [self.moviesList[x] for x in self.zipcodeList[zipcode]]
            # return ''.join(map(str, result))

        ids = self.GetMovieIDs(zipcode)
        titles = self.GetMovieTitles(zipcode)

        self.zipcodeList[zipcode] = ids

        for title, id in zip(titles, ids):
            self.CreateMovie(title, id)

        # result = [self.moviesList[x] for x in self.zipcodeList[zipcode]]
        # return ''.join(map(str, result))

    # ---------------------------------------------------------
    def CreateMovie(self, title, movieID):
    # ---------------------------------------------------------
        if movieID in self.moviesList:
            return
            #print 'Movie Already Seen ', movieID
        else:
            self.CreateActors(movieID)
            self.moviesList[movieID] = Movie(title,
                                             movieID,
                                             self.GetActorIDs(movieID))

    # ---------------------------------------------------------
    def CreateActors(self, movieID):
    # ---------------------------------------------------------
        names = self.GetActorNames(movieID)
        ids = self.GetActorIDs(movieID)

        for name, id in zip(names, ids):
            self.CreateActor(name, id, movieID)

    # ---------------------------------------------------------
    def CreateActor(self, name, id, movieID):
    # ---------------------------------------------------------
        if id in self.actorsList:
            return
            #print 'Actor Already Seen ', id
        else:
            self.actorsList[id] = Actor(name, id, [movieID])

    # ---------------------------------------------------------
    def SetAges(self, movieID):
    # ---------------------------------------------------------
        actorIDs = self.moviesList[movieID].actorIDs

        numberOfAges = 0
        total = 0

        for actorID in actorIDs:
            age = self.GetAge(actorID)
            if age > 0:
                numberOfAges += 1
                total += age

            self.actorsList[actorID].age = age

        self.moviesList[movieID].average = total / numberOfAges

    # Based on parsing
    #=============================
    # ---------------------------------------------------------
    def GetMovieTitles(self, zipcode):
    # ---------------------------------------------------------
        self.parser.Run('movie_title', zipcode)
        return self.parser.Get('movie_title')

    # ---------------------------------------------------------
    def GetMovieIDs(self, zipcode):
    # ---------------------------------------------------------
        self.parser.Run('movie_id', zipcode)
        return self.parser.Get('movie_id')

    # ---------------------------------------------------------
    def GetActorNames(self, movieID):
    # ---------------------------------------------------------
        self.parser.Run('actor_name', movieID)
        return self.parser.Get('actor_name')

    # ---------------------------------------------------------
    def GetActorIDs(self, movieID):
    # ---------------------------------------------------------
        self.parser.Run('actor_id', movieID)
        return self.parser.Get('actor_id')

    # ---------------------------------------------------------
    def GetAge(self, actorID):
    # ---------------------------------------------------------
        self.parser.Run('actor_age', actorID)
        age = self.parser.Get('actor_age')
        return int(age)

    # Print debug messages
    #=============================
    # ---------------------------------------------------------
    def PrintMovieTitles(self):
    # ---------------------------------------------------------
        return self.parser.Get('movie_title')

    # ---------------------------------------------------------
    def PrintMovieIDs(self):
    # ---------------------------------------------------------
        return self.parser.Get('movie_id')

    # ---------------------------------------------------------
    def PrintActorNames(self):
    # ---------------------------------------------------------
        return self.parser.Get('actor_name')

    # ---------------------------------------------------------
    def PrintActorIDs(self):
    # ---------------------------------------------------------
        return self.parser.Get('actor_id')

    # ---------------------------------------------------------
    def PrintActorAges(self):
     # ---------------------------------------------------------
        return self.parser.Get('actor_age')
