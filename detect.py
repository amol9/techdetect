import requests
import sys
from pprint import pprint
import re
from pdb import set_trace as pdbst

url = sys.argv[1]

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"
res = requests.get(url, headers={"User-Agent": ua})

x_powered_by = "X-Powered-By"
if x_powered_by in res.headers.keys():
    xpb = res.headers[x_powered_by]
    print(xpb)

    if xpb == "Express":
        print("Node.js")

amz_cf = "X-Amz-Cf"

for h in res.headers:
    if h.find(amz_cf) > -1:
        print("Amazon Cloudfront")
        break

source = res.content

def find_in_source(regex, source):
    #pdbst()
    r = re.compile(regex)
    m = r.findall(source)
    if len(m) > 0:
        return True
    else:
        return False

if find_in_source(b"script.*?ampproject.org", source):
    print("Accelarated Mobile Pages")
    print("Lighbox")

if find_in_source(b"fonts\.googleapis\.com", source):
    print("Google Font API")

if find_in_source(b"amazonaws\.com", source):
    print("AWS")

if find_in_source(b"youtube\.com", source):
    print("Youtube")

if find_in_source(b"facebook\.com", source):
    print("Facebook")

if find_in_source(b"instagram\.com", source):
    print("Instagram")

if find_in_source(b"amp-analytics", source) or find_in_source(b"googleanalytics", source):
    print("Google Analytics")

if find_in_source(b"googletagmanager\.com", source):
    print("Google Tag Manager")