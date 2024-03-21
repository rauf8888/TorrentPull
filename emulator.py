from colorama import Fore,Style
from bs4 import BeautifulSoup
from pprint import pprint
from tqdm import tqdm
import pandas as pd
import requests

site = requests.get("https://1337xto.to")
pprint(site)