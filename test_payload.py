# -*- coding: utf-8 -*-

import requests
import random

url = u"http://www.landchina.com/default.aspx"
querystring = {u"tabid":u"261",u"wmguid":u"20aae8dc-4a0c-4af5-aedf-cc153eb6efdf",u"p":u""}

user_agent_pool = [
    u'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    u'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    u'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    u'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    u'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    u'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    u'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    u'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    u'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
]
common_headers = {
    u'Accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    u'Accept-Encoding': u'gzip, deflate',
    u'Accept-Language': u'zh-CN,zh;q=0.9',
    u'User-Agent': random.choice(user_agent_pool),
    u'Host': u'www.landchina.com',
    u'Cookie': u'',
    u'Cache-Control': u'max-age=0',
    u'Connection': u'keep-alive',
    u'Referer': u'http://www.landchina.com/',
}

payload = u"__VIEWSTATE=%2FwEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhwFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBYwBQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X2NyZ2cyMDExTkhfMDEuZ2lmKTsfAwUCNDYWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwF%2BgY8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8%2BPC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE5IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI%2BDQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn%2BWcsOW4guWcuue9kSZuYnNwOyZuYnNwO%2BaKgOacr%2BaUr%2BaMgTrmtZnmsZ%2Foh7vlloTnp5HmioDogqHku73mnInpmZDlhazlj7gmbmJzcDs8YnIgLz4NCuWkh%2BahiOWPtzog5LqsSUNQ5aSHMDkwNzQ5OTLlj7cg5Lqs5YWs572R5a6J5aSHMTEwMTAyMDAwNjY2KDIpJm5ic3A7PGJyIC8%2BDQo8L3NwYW4%2BJm5ic3A7Jm5ic3A7Jm5ic3A7PGJyIC8%2BDQombmJzcDs8L3NwYW4%2BPC9wPh8BBWRCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3MjAxM195d18xLmpwZyk7ZGR7I32RK26Bk%2Bp6WD7UihTi82n4Qy4TZk2bR%2Fz3cOtrdA%3D%3D&__EVENTVALIDATION=%2FwEWAgKBpen4AgLN3cj%2FBB%2FGRZ3FMwMIVCBkr0t54XhYoKeBsRdsD9hHbSBE%2BRVy&hidComName=default&TAB_QueryConditionItem=894e12d9-6b0f-46a2-b053-73c49d2f706d&TAB_QueryConditionItem=598bdde3-078b-4c9b-b460-2e0b2d944e86&TAB_QueryConditionItem=87f11024-55ab-4faf-a0af-46371e33ae66&TAB_QueryConditionItem=6d2c89e6-b5a1-405d-8a71-2399e924d2c1&TAB_QuerySortItemList=c04b6ee6-3975-43ab-a733-28dcc4707112%3AFalse&TAB_QuerySubmitConditionData=894e12d9-6b0f-46a2-b053-73c49d2f706d%3A52%A8%88%7E%B9%F3%D6%DD%CA%A1%7C598bdde3-078b-4c9b-b460-2e0b2d944e86%3A2018-11-1%7E2019-6-2%7C6d2c89e6-b5a1-405d-8a71-2399e924d2c1%3A12460fc6e44e%7E%D7%A1%D5%AC&TAB_QuerySubmitOrderData=c04b6ee6-3975-43ab-a733-28dcc4707112%3AFalse&TAB_RowButtonActionControl=&TAB_QuerySubmitPagerData=1&TAB_QuerySubmitSortData="

headers = {
    u'Accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    u'Accept-Encoding': u'gzip, deflate',
    u'Content-Type': u"application/x-www-form-urlencoded",
    u'Accept-Language': u'zh-CN,zh;q=0.9',
    u'User-Agent': u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    u'Host': u'www.landchina.com',
    u'Cookie': u"ASP.NET_SessionId=s34ginv0cplzzo5xnscn4lxc; Hm_lvt_83853859c7247c5b03b527894622d3fa=1556964305,1556964305,1556964306,1559370971; srcurl=687474703a2f2f7777772e6c616e646368696e612e636f6d2f64656661756c742e617370783f74616269643d32363126776d677569643d32306161653864632d346130632d346166352d616564662d63633135336562366566646626703d; yunsuo_session_verify=9bc2f32623aadcc54e93ddbd8ed6e987; security_session_mid_verify=d4c7cd1a62f92cbe246f23cc7460a560; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1559483781",
    u'Cache-Control': u'max-age=0',
    u'Connection': u'keep-alive',
    u'Referer': u'http://www.landchina.com/default.aspx?tabid=261&wmguid=20aae8dc-4a0c-4af5-aedf-cc153eb6efdf&p=',
}
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
text = response.text
print(text.encode('utf-8'))
print'='*30
