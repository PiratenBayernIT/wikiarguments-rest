# -*- coding: utf-8 -*-
'''
Created on 01.01.2014
@author: tobixx0
'''
from __future__ import division, absolute_import, print_function
import logging

from wikiarguments_rest import make_app

app = make_app()

from wikiarguments_rest.datamodel import *
