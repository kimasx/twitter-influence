# -*- coding: utf-8 -*-
"""
MongoDB Client Setup
"""
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.twitter