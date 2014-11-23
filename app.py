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
from flask import Flask
app = Flask(__name__)

parser = None


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<zipcode>")
def listMovies(zipcode):
    parser.GetMovies(zipcode, 1)
    data = str(dict(zip(parser.PrintMovieIDs(), parser.PrintMovieTitles())))
    return data


@app.route("/actor/<actor_id>")
def actor(actor_id):
    parser.GetAge(actor_id)
    return str(parser.PrintActorAges())


@app.route("/movie/<movie_id>")
def movie(movie_id):
    parser.GetActors(movie_id)
    return str(parser.PrintActorNames()) + str(parser.PrintActorIDs())


@app.route("/movie/<movie_id>/full")
def movieFull(movie_id):
    return 'Full'
    #parser.GetActors(movie_id)
    #return str(parser.PrintActorNames()) + str(parser.PrintActorIDs())

if __name__ == "__main__":
    parser = MovieParser(IMDBParser())
    app.run(host='0.0.0.0', debug=True)
