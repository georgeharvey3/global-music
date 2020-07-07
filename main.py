# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 07:47:38 2020

@author: George
"""

from get_playlist_albums import get_albums
from build_urls import get_urls
from get_data import get_data
from insert_data import insert_data

album_tuples = get_albums('spotify:playlist:1a6AQnboGNuVNAVXkt060y')
urls = get_urls(album_tuples)
data_list = [get_data(url) for url in urls]
insert_data(data_list)