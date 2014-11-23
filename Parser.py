#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name: self.py
# Purpose: Scrape latest movies off IMDB and get average age of the actors
#
# Author: Matthew Sylvia (msylvia@nukefile.net)
#
# Created: 11/22/2014
# Copyright: (c) 2014 Matthew Sylvia
# Licence: MIT
#-----------------------------------------------------------------------------

from lxml import html
import requests


class Parser:
    'Information about a Movie'

    list = {}
    cached = {}

    # =========================================================
    def __default(self, val):
        return val

    # =========================================================
    def Add(self, key, template, xpath, callback=__default):
        self.list[key] = {
            'url_template': template,
            'xpath': xpath,
            'callback': callback,
            'value': None
        }

    # =========================================================
    def Remove(self, key):
        if (key in self.list):
            del self.list[key]

    # =========================================================
    def Clear(self):
        self.list.Clear()

    # =========================================================
    def Run(self, key, vars):
        if (key not in self.list) or (vars is None):
            print key, " Not found"
            return

        # Build URL
        url = self.list[key]['url_template'].format(vars)

        tree = None

        # Check cache so we dont need to download the page again
        if url not in self.cached:
            # Make Request
            page = requests.get(url)
            tree = html.fromstring(page.text)

            self.cached[url] = tree
        # Already cached
        else:
            print url, " Already cached"
            tree = self.cached[url]

        # Parse
        rawValues = tree.xpath(self.list[key]['xpath'])

        # PostProcess if nessary
        self.list[key]['value'] = self.list[key]['callback'](self, rawValues)

    # =========================================================
    def Get(self, key):
        return self.list[key]['value']

    # =========================================================
    def PostProcess(self, value):
        return value
