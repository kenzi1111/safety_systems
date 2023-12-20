# import requests
# from django.conf import settings


# def get_coordinates_for_address(address):
#     api_key = settings.GOOGLE_MAPS_API_KEY
#     base_url = "https://maps.googleapis.com/maps/api/geocode/json"
#     response = requests.get(base_url, params={"address": address, "key": api_key})
#     response_json = response.json()

#     if response_json["status"] == "OK":
#         result = response_json["results"][0]
#         latitude = result["geometry"]["location"]["lat"]
#         longitude = result["geometry"]["location"]["lng"]
#         return latitude, longitude
#     else:
#         return None, None
