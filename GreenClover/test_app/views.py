from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
import requests
from rest_framework import generics
from test_app.models import Snippet
from test_app.serializers import SnippetSerializer
from rest_framework.parsers import JSONParser
import io
from dadata import Dadata
from geopy.distance import geodesic
from math import ceil, pi, cos
from datetime import datetime
from geopy.geocoders import Nominatim


def get_metro(metro):
    token = "353a3d637266d50552f4534af4a839d507e6f5e5"
    dadata = Dadata(token)
    result = dadata.suggest("metro", metro)
    return result


def calculate_distance_km(metro_latitude, metro_longitude, place_latitude, place_longitude):
    gps_point_1 = (metro_latitude, metro_longitude)
    gps_point_2 = (place_latitude, place_longitude)
    return geodesic(gps_point_1, gps_point_2).meters


def get_time(metro_latitude, metro_longitude, place_latitude, place_longitude):
    time = ceil(calculate_distance_km(metro_latitude,
                metro_longitude, place_latitude, place_longitude) / 83.3)
    return time


def define_location_degrees(address: str):
    geolocator = Nominatim(user_agent='SPb_degrees')
    if address != '':
        location = geolocator.geocode(address)
        return location.latitude, location.longitude, location.address
    return None, None, None

def define_location_name(latitude, longitude):
    geolocator = Nominatim(user_agent='SPb_name')
    location = geolocator.reverse(f'{latitude}, {longitude}')
    return location.address

# def get_stops_near(latitude, longitude):
#     earth_radius = 6371 * 1000
#     difference = (200 / earth_radius) * (180 / pi)
#     max_latitude = latitude + difference
#     max_longitude = longitude + difference / cos(latitude * pi/180)
#     min_latitude = latitude - difference
#     min_longitude = longitude - difference / cos(latitude * pi/180)
#     token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhU1RaZm42bHpTdURYcUttRkg1SzN5UDFhT0FxUkhTNm9OendMUExaTXhFIn0.eyJleHAiOjE3Nzg1MjM2NDEsImlhdCI6MTY4MzgyOTI0MSwianRpIjoiYWRiMzIwYjMtYjIzMy00OTYyLTg1ZWQtYzdlNjY2NzAyNzcwIiwiaXNzIjoiaHR0cHM6Ly9rYy5wZXRlcnNidXJnLnJ1L3JlYWxtcy9lZ3MtYXBpIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjEzZjZiODViLWM1MGUtNDI0ZS1hNzhjLTliYTc0NzdhN2I0NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLXJlc3QtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImIzZjhlMmFhLTMwZDktNGNjMy1iNjAyLWM4YjU3MGRmOTQ3MiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZWdzLWFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiM2Y4ZTJhYS0zMGQ5LTRjYzMtYjYwMi1jOGI1NzBkZjk0NzIiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQkNC90LTRgNC10Lkg0K_Qs9C40L0iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiI1YjVjMGFmZWU3NGQwOGY5YzViYzg5MzQ1YmNmMTUxYSIsImdpdmVuX25hbWUiOiLQkNC90LTRgNC10LkiLCJmYW1pbHlfbmFtZSI6ItCv0LPQuNC9In0.1Zn6hB_TfDjIGmBv5CsQ3fTGnUoW5Ae7tx0YoY1Z61Eo9IR2u8vfPFbKn4Ju0Z5_wWvz1Xhos1Voz5GtZb8_Q0SnIX1hYbpBEd5VmcuijnsVa6IHF7ky6J3JDlp-fgALBJ-au7Qj5qSkGwtCnmVsV1cf1RfAodmlR3RLLQX8T1_08uidnDxiZqgEnlBVp2PMy9GGLX-WJFT6MCrg8Q7OUxHj7lZPsSRmIQIa0NVoV-09cH1RRSJKgvPPnfRZsppKG04rrPX9ECEDQlaDU4nYVX-p_Zt0JPvrzbpeX3i8Enh1FJsKHfRG83WQXyCDzJZOqO_5Hmo4AN8p2ACg5cc9kQ'
#     url = f'https://spb-transport.gate.petersburg.ru/api/vehicles/{min_longitude},{min_latitude},{max_longitude},{max_latitude}'
#     response = requests.get(url, headers={'Authorization': token})
#     routes = [transport['routeId'] for transport in response.json()['result']]
#     stops = set()
#     for route in routes:
#         url_to = f'https://spb-transport.gate.petersburg.ru/api/stops/{route}/0'
#         response_to = requests.get(url_to, headers={'Authorization': token}).json()
#         for coordinates in response_to['result'][0]['path']:
#             if min_latitude <= coordinates['lat'] <= max_latitude and\
#                   min_longitude <= coordinates['lon'] <= max_longitude:
#                 stops.add(define_location_name(str(coordinates['lat']), str(coordinates['lon'])))
#             if len(stops) == 2:
#                 break
        
#         url_from = f'https://spb-transport.gate.petersburg.ru/api/stops/{route}/1'
#         response_from = requests.get(url_from, headers={'Authorization': token}).json()
#         for coordinates in response_from['result'][0]['path']:
#             if min_latitude <= coordinates['lat'] <= max_latitude and\
#                   min_longitude <= coordinates['lon'] <= max_longitude:
#                 stops.add(define_location_name(coordinates['lat'], coordinates['lon']))
#             if len(stops) == 4:
#                 break
#     return list(stops)
        
def get_info(request: HttpRequest):
    raw_info = io.BytesIO(request.body)
    info = JSONParser().parse(raw_info)
    start = datetime(*list(map(int, info['dates'].split('-'))))
    is_free = 'true' if info['isFree'] else 'flase' 
    kilometers = int(info['km'])
    latitude, longitude, addr = define_location_degrees(info['address'])
    if not latitude:
        latitude, longitude = '59.939016', '30.31588'
    page = info['page']
    url = f'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/events?lat={latitude}&lng={longitude}&radius={kilometers}&fields=categories%2Cdescription%2Cplace%2Ctitle%2Cage_restriction%2Cis_free%2Cimages%2Cprice%2Cdates&expand=images%2Cplace%2Clocation%2Cdates%2Cparticipants&page={page}&count=12&is_free={is_free}&actual_since={start}'
    BLOCK_IMAGE_INFO = 'https://kudago.com/media/images/event/82/bb/82bb410cca413007c5598f40c6ebd68c.jpg'
    response = requests.get(url, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhU1RaZm42bHpTdURYcUttRkg1SzN5UDFhT0FxUkhTNm9OendMUExaTXhFIn0.eyJleHAiOjE3Nzg1MjM2NDEsImlhdCI6MTY4MzgyOTI0MSwianRpIjoiYWRiMzIwYjMtYjIzMy00OTYyLTg1ZWQtYzdlNjY2NzAyNzcwIiwiaXNzIjoiaHR0cHM6Ly9rYy5wZXRlcnNidXJnLnJ1L3JlYWxtcy9lZ3MtYXBpIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjEzZjZiODViLWM1MGUtNDI0ZS1hNzhjLTliYTc0NzdhN2I0NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLXJlc3QtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImIzZjhlMmFhLTMwZDktNGNjMy1iNjAyLWM4YjU3MGRmOTQ3MiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZWdzLWFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiM2Y4ZTJhYS0zMGQ5LTRjYzMtYjYwMi1jOGI1NzBkZjk0NzIiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQkNC90LTRgNC10Lkg0K_Qs9C40L0iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiI1YjVjMGFmZWU3NGQwOGY5YzViYzg5MzQ1YmNmMTUxYSIsImdpdmVuX25hbWUiOiLQkNC90LTRgNC10LkiLCJmYW1pbHlfbmFtZSI6ItCv0LPQuNC9In0.1Zn6hB_TfDjIGmBv5CsQ3fTGnUoW5Ae7tx0YoY1Z61Eo9IR2u8vfPFbKn4Ju0Z5_wWvz1Xhos1Voz5GtZb8_Q0SnIX1hYbpBEd5VmcuijnsVa6IHF7ky6J3JDlp-fgALBJ-au7Qj5qSkGwtCnmVsV1cf1RfAodmlR3RLLQX8T1_08uidnDxiZqgEnlBVp2PMy9GGLX-WJFT6MCrg8Q7OUxHj7lZPsSRmIQIa0NVoV-09cH1RRSJKgvPPnfRZsppKG04rrPX9ECEDQlaDU4nYVX-p_Zt0JPvrzbpeX3i8Enh1FJsKHfRG83WQXyCDzJZOqO_5Hmo4AN8p2ACg5cc9kQ'})

    if response.status_code == 200:
        data = response.json()
        for item in data['data']:
            # item['stops'] = get_stops_near(
            #     item['place']['coords']['lat'], item['place']['coords']['lon'])
            if item['images'][0]['image'] == BLOCK_IMAGE_INFO:
                item['images'] = False
            item['description_full'] = item['description']
            item['description'] = item['description'][1:101] + '...'
            subway = item['place']['subway'].split(',')
            if len(subway) != 1:
                item['place']['subway'] = subway[0]
            item['subway_info'] = get_metro(item['place']['subway'])
            for subway_info in item['subway_info']:
                item['subway_time'] = get_time(subway_info['data']['geo_lat'], subway_info['data']
                                               ['geo_lon'], item['place']['coords']['lat'], item['place']['coords']['lon'])

    return data


def events(request: HttpRequest):
    # return HttpResponse(get_info(request))
    if request.method == 'POST':
        data = get_info(request)
        return JsonResponse({'data': data})
    return HttpResponse("Error")
    # stream = io.BytesIO(request.body)
    # json_str = JSONParser().parse(stream)
