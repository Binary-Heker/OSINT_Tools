# Description: This script is used to get the basic information of a phone number.
# Author: KaliHeker

import requests

key = 'KEY'
country_code = '91'
phone_number = 'INPUT'
url = 'https://api.veriphone.io/v2/verify?phone=%2B'+country_code+'-'+phone_number+'&key='+key+''

response = requests.get(url);
data = response.json()

# Country Code
country_code = str(data['country_code'])
print("Country Code -> "+country_code) 

# Phone Number
phone_number = str(data['e164'])
print("Phone Number -> "+phone_number)

# Phone Type
phone_type = str(data['phone_type'])
print("Phone Type -> "+phone_type)

# Carrier
carrier = str(data['carrier'])
print("Carrier -> "+carrier)