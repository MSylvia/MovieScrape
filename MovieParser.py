#!/usr/bin/python

from lxml import html
import requests
from Movie import *
from Actor import *


class MovieParser:
    'Get movies by zipcode. Can limit number of movies returned.'

    actorsList = {}
    moviesList = {}

    # Get movies based on zipcode
    #=============================
    def GetMovies(self, zipcode, num=0):

        template = 'http://www.imdb.com/showtimes/location/US/{0}?sort=alpha'

        movieIDs = []

        url = template.format(zipcode)

        page = requests.get(url)
        tree = html.fromstring(page.text)

        # List of movie names
        rawTitles = tree.xpath('//*[@class="title"]/a/text()')
        # Actors
        rawLinks = tree.xpath('//*[@class="title"]/a')

        index = num

        for title, link in zip(rawTitles, rawLinks):
            # Check to make sure we care
            if index > 0 and num != 0:
                # Get parsed values
                movie_ID = link.attrib['href'].split('/')[3]

                # Add to global List
                if movie_ID in MovieParser.moviesList:
                    print 'Movie Already Seen'
                else:
                    MovieParser.moviesList[movie_ID] = Movie(
                        title, movie_ID, MovieParser.GetActors(self, movie_ID))
                    movieIDs.append(movie_ID)

            if num != 0:
                index -= 1

        return movieIDs

    # Get actors based on movie id
    #=============================
    def GetActors(self, movieID):

        titleURLFormat = 'http://www.imdb.com/title/{0}/fullcredits'

        actorIDs = []

        page = requests.get(titleURLFormat.format(movieID))
        tree = html.fromstring(page.text)

        rawActorsElem = tree.xpath('//*[@itemprop="actor"]/a')

        # print len(rawActorsElem)

        for actorElem in rawActorsElem:
            # Get parsed values
            actor_name = actorElem.find('span').text
            actor_ID = actorElem.attrib['href'].split('/')[2]

            # Check if actor has been seen before
            if actor_ID in MovieParser.actorsList:
                MovieParser.actorsList[actor_ID].movieIDs.append(movieID)
            # New actor
            else:
                # Add to global List
                MovieParser.actorsList[actor_ID] = Actor(
                    actor_name, actor_ID, [movieID])
                actorIDs.append(actor_ID)

        return actorIDs
