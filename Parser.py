#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name: Parser.py
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

    # =========================================================
    def __default(val):
        return val

    # =========================================================
    def Add(self, key, template, vars, xpath, callback=__default):
        Parser.list[key] = {
            'url_template': template,
            'url_vars': vars,
            'xpath': xpath,
            'callback': callback,
            'value': None
        }

    # =========================================================
    def Process(self, key):
        # Build URL
        url = Parser.list[key]['url_template'].format(
            Parser.list[key]['url_vars'])

        # Make Request
        page = requests.get(url)
        tree = html.fromstring(page.text)

        # Parse
        rawValues = tree.xpath(Parser.list[key]['xpath'])

        # PostProcess if nessary
        Parser.list[key]['value'] = Parser.list[key]['callback'](rawValues)

    # =========================================================
    def Get(self, key):
        return Parser.list[key]['value']

    # =========================================================
    def PostProcess(self, value):
        return value
