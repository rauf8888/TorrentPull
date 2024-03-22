from colorama import Fore,Style
from bs4 import BeautifulSoup
from pprint import pprint
from tqdm import tqdm
import pandas as pd
import requests

proxies = {'https':'https://103.88.44.21:80'}

site = requests.get("https://ipinfo.io/json",proxies=proxies)
print(site.text)
