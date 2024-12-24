def domain_name(url):
    if "://" in url:
        url = url.split("://")[1]

    url = url.split('/')[0]

    if url.startswith('www.'):
        url = url[4:]
    if url.endswith('.com'):
        url = url[:-4]
    elif url.endswith('.ru'):
        url = url[:-3]
    elif url.endswith('.org'):
        url = url[:-4]
    elif url.endswith('.net'):
        url = url[:-4]
    elif ".co" in  url:
        url = url.split('.')[0]
    elif "." in  url:
        url = url.split('.')[0]
    return url

print(domain_name("asft31n3rc2polzmrq6m.edu"))