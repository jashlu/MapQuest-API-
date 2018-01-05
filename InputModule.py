import json
import urllib.parse
import urllib.request
from collections import namedtuple
import apiconsole
import APIs 





def get_location():
    '''ask for location input'''
    while True:
        try:
            num = int(input(''))
            locations = []
            while len(locations) < num:
                item = input()
                locations.append(item)
            return locations
            
        except ValueError:
            print('Not Valid')




def get_output():
    '''ask for location input'''
    while True:
        try:
            num2 = int(input(''))
            outputs = []
            while len(outputs) < num2:
                single = input()
                outputs.append(single)           
            return outputs
        except ValueError:
            print('Not Valid')



                        
def convert_functions(outputs: ['outputs']) -> list:
     '''convert the desired outputs in str into intended functions'''
     ordered_list = []
     
     for x in outputs:
          if x == 'LATLONG':
              ordered_list.append(apiconsole.LatLng())
          elif x == 'STEPS':
              ordered_list.append(apiconsole.Directions())
          elif x == 'TOTALTIME':
              ordered_list.append(apiconsole.Time())
          elif x == 'TOTALDISTANCE':
              ordered_list.append(apiconsole.Distance())
          elif x == 'ELEVATION':
              ordered_list.append(apiconsole.Elevation())
     return ordered_list                                                       




def run_game():
    '''this module will run the program, ask for input and display wanted
    results'''
    locay = get_location()
    outputs = get_output()
    url = APIs.build_search_url(locay)
    data = APIs.get_result(url)
    
    elev_results = apiconsole.LatLng().elevation_calc(data)
    compressed_list = APIs.elevation_latlong(elev_results)
    print(url)
    print(compressed_list)
    elev_url_list = APIs.build_elevation_url(compressed_list)
    print(elev_url_list)
    elev_data = APIs.get_elev_results(elev_url_list)
    
    converted_functions = convert_functions(outputs)
    
    for function in converted_functions:
        try:
            function.calculate(data)
        except:
            function.calculate(elev_data)
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')






if __name__ == '__main__':
    run_game() 
  


