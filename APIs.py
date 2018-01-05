#Project 3
#Joshua Lu
#60343957

import json
import urllib.parse
import urllib.request
import sys


API_KEY = 'ALdGQdL80D53ZodxGegWkdANO4zsRLBq'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'

BASE_MAPQUEST_URL_2 = 'http://open.mapquestapi.com/elevation/v1'





def build_search_url(locations:list) -> str:
    '''
    This function takes a search query and the maximum number of results
    to display, and builds and returns a URL that can be used to ask the
    mapquest API.
    '''
    query_parameters = [
        ('key', API_KEY), ('from', locations[0]),
        ('to', locations[1])]

    for x in locations:
        if locations.index(x) > 1:
            query_parameters.append(('to', x))       

    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(query_parameters)


def elevation_latlong(result:list) -> list:
    '''this extra step is to help create multiple urls to surpass the maximum distance
    inhibitor for the MapQuest elevation API'''

    try:
        mini_list = []

        for x in range(0, len(result), 2):
            compressed = ''
            compressed += str(str(result[x]) + ',' + str(result[x+1]))

            mini_list.append(compressed)
    
        return mini_list
    
    except:
        print('NO ROUTE FOUND')
        sys.exit()
    
            
       

def build_elevation_url(result:list) -> list:
    '''
    This function takes a search query and the maximum number of results
    to display, and builds and returns a URL that can be used to ask the
    mapquest API.
    '''
    try:
        all_elev_urls = []

        for x in range(len(result)):
            str1 = result[x]

   
            query_parameters = [
                ('key', API_KEY), ('shapeFormat', 'raw'), ('latLngCollection', '')
                ]
            url = BASE_MAPQUEST_URL_2 + '/profile?' + urllib.parse.urlencode(query_parameters) + str1
     
            all_elev_urls.append(url)
        return all_elev_urls

    except TypeError:
        sys.exit()




def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None
    
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        
        data = json.loads(json_text)
        return data 
 
    finally:

        if response != None:
            response.close()


def get_elev_results(url_list:list) -> list:
    ''' This function takes elev url and returns dictionary representing JSON reponse'''
    response = None
    elev_data_list = []
    try:
        for x in url_list:
            response = urllib.request.urlopen(x)
            json_text = response.read().decode(encoding = 'utf-8')
            
            data = json.loads(json_text)
            
            elev_data_list.append(data)
            
        return elev_data_list
    finally:
        if response != None:
            response.close()
