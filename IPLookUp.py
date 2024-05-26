# Description: This script is used to get information of an IP address.
# Author: KaliHeker

import requests

ip_address = 'INPUT'
key = 'a924a2a6f5fa447a968cbfb379de762e'

url = 'https://api.ipgeolocation.io/ipgeo?apiKey='+key+'&ip='+ip_address
response = requests.get(url)
data = response.json()

    
# IP Address
ip = str(data['ip'])
print("IP Address -> "+ip) 
    
# Country
country = str(data['country_name'])
print("Country -> "+country)
    
# Country Code
country_code = str(data['country_code3'])
print("Country Code -> "+country_code)
    
# Region
region = str(data['state_prov'])
print("Region -> "+region)
    
    
# City
city = str(data['city'])
print("City -> "+city)
    
# Zip Code
zip_code = str(data['zipcode'])
print("Zip Code -> "+zip_code)
    
# Latitude
lat = str(data['latitude'])
print("Latitude -> "+lat)
    
# Longitude
lon = str(data['longitude'])
print("Longitude -> "+lon)
    
# ISP
isp = str(data['isp'])
print("ISP -> "+isp)
    
# Organization
org = str(data['organization'])
print("Organization -> "+org)