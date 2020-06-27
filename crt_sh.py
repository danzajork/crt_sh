#!/usr/bin/python3
import requests, json, sys
target = sys.argv[1].rstrip()

parsed_domains = []

req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))
json_data = json.loads(req.text)

for (key,value) in enumerate(json_data):
    domains = value['name_value'].replace('*.', '').splitlines()
    for d in domains:
        if d not in parsed_domains:
            if d.endswith('.com'):
                parsed_domains.append(d)

for d in parsed_domains:
    print(d)