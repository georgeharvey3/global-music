from bs4 import BeautifulSoup
import requests
from collections import defaultdict


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }


def get_data(pages):

    """Scrapes album details from a web page and packages them into a dictionary.

    Args:
        page (str): The url of the web page containing the album details.

    Returns:
        return_d (dict): dictionary containing the key information about the album.

    Raises:
        HTTPError: If web page URL is not found.
        IndexError: If page does not have the title element.
    """
    
    for page in pages:

        res = requests.get(page, headers=headers, verify=False)
        
        if res.status_code != 200:
            print('Web site does not exist') 
            res.raise_for_status()
            
        soup = BeautifulSoup(res.text, 'html.parser')
        
        d = {}
        
        title = soup.findAll("h1", {"class": "title"})
        title_text = BeautifulSoup.get_text(title[0])    
        d['title'] = title_text
        
        mydivs = soup.findAll("div", {"class": "album-info"})
        
        fields = ['Language(s)', 'Instrument(s)', 
                  'Culture Group(s)', 'Country(s)',
                  'Year(s) Released', 'Recording Location(s)']
        
        for div in mydivs:
            div_text = BeautifulSoup.get_text(div)
            for field in fields:
                if field in div_text:
                    result = div.findAll("div", {"class": "copy"})
                    d[field] = BeautifulSoup.get_text(result[0]).strip()
                
        liner = soup.findAll("a", {"class": "last-sidebar-item"})
        try:
            d['liner'] = liner[0]['href']
        except IndexError:
            d['liner'] = 'None'
        
        
        return_d = {'ethnic_groups': (d.get('Country(s)', 'None') + ' - ' + d.get('Culture Group(s)') 
                              if d.get('Culture Group(s)') else d.get('Country(s)', 'None')),
                    'album_title': (d['title'] + ' (' + d.get('Year(s) Released') + ')'
                                    if d.get('Year(s) Released') else d['title']),
                    'languages': d.get('Language(s)', 'None'),
                    'instruments': d.get('Instrument(s)', 'None'),
                    'liner': d['liner'],
                    'location': d.get('Recording Locations(s)', 'None')}
 
        yield return_d





            
    

