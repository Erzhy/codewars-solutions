import re

def domain_name(url):
    return re.search(r'(https)?(http)?(://)?(www)?\.?(.*?)\.', url).group(5)
