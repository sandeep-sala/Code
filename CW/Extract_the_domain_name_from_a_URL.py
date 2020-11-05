def domain_name(url):
    return url.replace("https://","").replace("http://","").replace("www.","").split(".")[0]



print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")