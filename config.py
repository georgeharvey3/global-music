# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:15:47 2020

@author: George
"""

def get_playlist_name():
    """Reads playlist name from text file in convevient location for editing

    Returns:
        name (str): The name of the playlist to be operated upon
    """

    with open('C:\\Users\\George\\Desktop\\spotify_playlist.txt', 'r') as f:
        name = f.readlines()[0]

    return name

USERNAME = 'effilyg'  # your spotify username
CLIENT_ID = '8f4eb11b9f704a1c8dca356698b067f3'  # set at your developer account
CLIENT_SECRET = 'ad896f7b86084d2abab43243d39fcbe5'  # set at your developer account
REDIRECT_URI = 'http://google.com/'
PLAYLIST_NAME = 'Central Asia' #get_playlist_name()
SCOPE = 'playlist-read-private'
