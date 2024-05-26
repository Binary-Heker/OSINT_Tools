# IP and Phone Information Lookup

This project contains two Python scripts that fetch and display information about an IP address and a phone number.

## Scripts

1. [IPLookUp.py](IPLookUp.py): This script fetches and displays information about an IP address. The information includes the IP address, country, country code, region, city, zip code, latitude, longitude, ISP, and organization.

2. [BasicPhoneInfo.py](BasicPhoneInfo.py): This script fetches and displays basic information about a phone number. The information includes the country code, phone number, phone type, and carrier.

## Usage

To use these scripts, you need to replace the 'INPUT' in the `ip_address` and `phone_number` variables with the IP address and phone number you want to look up, respectively. Also, replace 'KEY' in the `key` variable with your API key.

## Dependencies

These scripts depend on the `requests` Python library. You can install it using pip:

```sh
pip install requests
```