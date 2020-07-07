# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:18:36 2020

@author: George
"""

import spotipy
import spotipy.util as util
import config
from collections import namedtuple

token = util.prompt_for_user_token(username=config.USERNAME, scope=config.SCOPE,
                                   client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET,
                                   redirect_uri=config.REDIRECT_URI)

# create spotifyObject
spotifyObject = spotipy.Spotify(auth=token)


def get_playlist_tracks(playlist_id):

    """Finds every track element Spotify playlist.

    Args:
        playlist_id (str): Spotify URI of the playlist to be searched.

    Returns:
        tracks (list): List of dictionaries containing information about each track on the playlist.
    """

    results = spotifyObject.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotifyObject.next(results)
        tracks.extend(results['items'])
    return tracks

def get_albums(playlist_id):

    """Evaluates track dictionaries and extracts the album name and artist name.

    Args:
        playlist_id (str): Spotify URI of the playlist to be searched.

    Returns:
        nts (list): List of named tuples containing the track album and track artist.

    """
    
    items = get_playlist_tracks(playlist_id=playlist_id)
        
    track_values = []
    
    for item in items:
        track = item['track']
        album = track['album']
        artists = tuple(artist['name'] for artist in album['artists'])
        
        track_values.append((album['name'], artists[0]))
    
    album_details = namedtuple('AlbumDetails', 'album artist')
    
    nts = [album_details(*tup) for tup in set(track_values)]
    
    return nts


