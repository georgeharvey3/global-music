# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 06:56:03 2020

@author: George
"""

from googlesearch import search


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

def get_urls(nts):

    """Uses track details to build a list of web pages to be searched.
    
    Args:
        nts (list): List of named tuples whose values will be used to build the URL.
    
    Returns:
        urls (list): List of URLs that contain details about an album.
    """
    urls = []
    
    for nt in nts:
                        
        query = nt.album + ' smithsonian'
        
        pages = list(search(query, tld='com', lang='en', 
                      num=3, start=0, stop=3, pause=2.0))
        for page in pages:
            if 'smithsonian' in page and 'album' in page:
                urls.append(page)
                break
        else:
            print('No page found for:', nt.album)
    return urls


        