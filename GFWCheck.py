#!/usr/bin/env python3
#coding=utf-8

import sys
import re
import os
import dns.resolver
import requests
import hashlib
from urllib.parse import urlparse, urljoin

def dnsCheck(url, query_type="A"):
    address = []
    my_resolver = dns.resolver.Resolver()

    try:
        host_a = my_resolver.query(url, query_type)
        if query_type == 'A':
            for i in host_a.response.answer:
                for j in i.items:
                    if re.match("^[0-9.]+$", str(j)):
                        address.append(str(j))
        elif query_type == 'TXT':
            txt_info = str(host_a.response.to_text())
            for line in txt_info.split("\n"):
                if url in line:
                    line = line.split()[-1]
                    if line != "TXT":
                        line = re.sub("\"|\'", "", line)
                        address.append(line)

    except Exception as e:
        print(str(e))
    return address

def getMd5(fname):
    md5 = None
    if os.path.isfile(fname):
        with open(fname,'rb') as f:
            md5_obj = hashlib.md5()
            md5_obj.update(f.read())
            hash_code = md5_obj.hexdigest()
    md5 = str(hash_code).lower()
    return md5


def fwxzWebCheck(url):
    try:
        r = requests.get(urljoin("http://%s" % url, ".well-known/acme-challenge/a.txt"))
    except:
        return None, ""
    url = r.url
    info = urlparse(url)
    url = info.netloc
    tmpFile = os.path.join("/tmp", "%s_download.txt" % url)
    with open(tmpFile, "w") as fobj:
        fobj.writelines(r.text)
    md5 = getMd5(tmpFile)
    return url, md5

def indexWebCheck(url):
    try:
        r = requests.get("http://%s" % url, timeout=60)
    except:
        return None, ""
    url = r.url
    info = urlparse(url)
    url = info.netloc
    tmpFile = os.path.join("/tmp", "%s_download.txt" % url)
    with open(tmpFile, "w") as fobj:
        fobj.writelines(r.text)
    md5 = getMd5(tmpFile)
    return url, md5

def getCheckRet(url):
    return dnsCheck(url), fwxzWebCheck(url)
    # return dnsCheck(url), indexWebCheck(url)

def main(urls):
    retDict = {}
    for u in urls:
        _, checkVal = fwxzWebCheck(u)
        # ret = getCheckRet(u)
        if checkVal == "ba1f2511fc30423bdbb183fe33f3dd0f":
            retDict[u] = True
        else:
            retDict[u] = False

    return retDict

if __name__ == "__main__":
    infos = main(sys.argv[1:])
    print(infos)
    sys.exit(0) if infos else sys.exit(1)
