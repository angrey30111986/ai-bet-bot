import os
import urllib.request

URL = "https://www.football-data.co.uk/mmz4281/2425/E0.csv"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE_DIR, "E0.csv")

print("Downloading...")

urllib.request.urlretrieve(URL, OUT)

print("Saved:", OUT)
