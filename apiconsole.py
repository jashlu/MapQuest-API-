#Project 3
#Joshua Lu
#60343957

import sys

class Elevation:

     def calculate(self, data: list) -> dict:
        'grab the longitude and latitude'''
        try:
             elev_results = []
             for elev_data in data:
                  elevations = []
                  for x in elev_data['elevationProfile']:
                       y = x['height']
                       converted = round(y*(3.3))
                       elev_results.append(converted)
       
             print()
             print('ELEVATIONS')             
             for x in elev_results:
                  print(x)
                  
        except KeyError:
             print('NO ROUTE FOUND')
             sys.exit()

            
class LatLng:
    
    def calculate(self, data: dict) -> dict:
        'grab the longitude and latitude'''
        print()
        print('LATLONGS')
        try:           
            for x in data['route']['locations']:
                data = x['latLng']
                lng = round(data['lng'], 2)
                lng1 = str(lng)
                lat = round(data['lat'], 2)
                print('{}N {}W'.format(lat,lng1[1:]))

        except KeyError:
            print('NO ROUTE FOUND')
            sys.exit()
   

        
    def elevation_calc(self, data:dict):
        '''isolate longitude and latitude, so I can figure out the elevation'''
        result = []
        try:
            for x in data['route']['locations']:
                data = x['latLng']
                lng = data['lng']
                lat = data['lat']
                
                lng1 = str(lng)
                lat1 = str(lat)
                
                result.append(lat1)
                result.append(lng1)
                
            return result

        except KeyError:
            print('NO ROUTE FOUND')
            sys.exit()               
        
            

class Directions:
    
    def calculate(self, data: dict) -> dict:
        '''grab the directions'''
        try:
             print()
             print('DIRECTIONS')
             for x in data['route']['legs']:
                  for y in x['maneuvers']:
                       print(y['narrative'])
                       
        except KeyError:
             print('NO ROUTE FOUND')
             sys.exit()

    


class Time:
    
    def calculate(self, data: dict) -> dict:
        '''grab the estimated time'''
        try:
             x = data['route']['time']
             length = x/60
             print()
             print('TOTAL TIME:', round(length), 'minutes')
             
        except KeyError:
             print('NO ROUTE FOUND')
             sys.exit()


class Distance:
    
    def calculate(self, data: dict) -> dict:
        '''grab the estimated distance'''
        try:
             length = data['route']['distance']
             
             if length %1 > 0.5:
                  print()
                  print('TOTAL DISTANCE:', int(length//1) + 1,'miles')
             else:
                  if length %1 < 0.5:
                       print()
                       print('TOTAL DISTANCE:', int(length//1),'miles')
                       
        except KeyError:
             print('NO ROUTE FOUND')
             sys.exit()
       

    

