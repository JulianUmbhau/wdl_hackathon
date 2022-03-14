# %%
import os
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import requests
#import dill
from bs4 import BeautifulSoup
#from datetime import datetime
import urllib.parse
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring

# %%
start_url="https://traffic.api.here.com/traffic/6.2/flow.xml?app_id="
access_id="yyxDuemlhkqdrTN-hC5BPg"
url_code="&app_code="
access_key="PpwpgkIZB7R3IagJQ1xbxoWFyNljdkM1B9RwVWMU4Q9RAc7th-u_Pcw9d0pAcE2xG0i6lWNBp_ZBc4ChM5C-Dw"
location_box="&bbox=39.039696,-77.222108;38.775208, -76.821107&responseattributes=sh,fc"
url_path=start_url+access_id+url_code+access_key+location_box

# %%
page = requests.get(url_path)
page = requests.get('https://traffic.api.here.com/traffic/6.2/flow.xml?app_id=yyxDuemlhkqdrTN-hC5BPg&app_code=PpwpgkIZB7R3IagJQ1xbxoWFyNljdkM1B9RwVWMU4Q9RAc7th-u_Pcw9d0pAcE2xG0i6lWNBp_ZBc4ChM5C-Dw&bbox=39.039696,-77.222108;38.775208, -76.821107&responseattributes=sh,fc')
soup = BeautifulSoup(page.text, "html.parser")

soup.text

#roads = soup.find_all('fi')
# %%
