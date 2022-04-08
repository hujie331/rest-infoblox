import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = "https://infoblox.sie.sony.com/wapi/v2.11.3/zone_forward"

payload={}
headers = {
  'Authorization': 'Basic amh1MTpIVWppZUAyMDIyMDIyNw==',
  'Cookie': 'ibapauth="group=SIE-Infoblox-IT-NetEng,ctime=1649395059,ip=10.58.206.126,auth=AD,client=API,user=jhu1,timeout=86400,mtime=1649395906,QwOFJICVTSfhTnilk2d9H205q813YQN21fI"'
}

response = requests.request("GET", url, verify=False, headers=headers, data=payload)
json_data = response.json()
pprint(json_data)
# print(response.text)