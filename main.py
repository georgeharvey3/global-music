# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 07:47:38 2020

@author: George
"""

from get_playlist_albums import get_albums
from build_urls import get_urls
from get_data import get_data
from insert_data import insert_data

import config



def pipeline(playlist_name):
    album_tuples = get_albums(playlist_name)
    urls = get_urls(album_tuples)
    data = get_data(urls)
    
    yield from data

if __name__ == '__main__':
    for data in pipeline(config.PLAYLIST_NAME):
        insert_data(data)
    