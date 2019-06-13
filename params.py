# -*- coding: utf-8 -*-

import re
import random
import requests

user_agent_pool = [
    # u'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    # u'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    # u'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    # u'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    # u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    # u'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    # u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # u'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # u'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    # u'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    # u'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    # u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    # u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    # u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    # u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    # u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    # u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    # u'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
]

common_headers = {
    u'Accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    u'Accept-Encoding': u'gzip, deflate',
    u'Accept-Language': u'zh-CN,zh;q=0.9',
    u'Content-Type': u"application/x-www-form-urlencoded",
    u'User-Agent': random.choice(user_agent_pool),
    u'Host': u'www.landchina.com',
    u'Cookie': u'',
    u'Cache-Control': u'max-age=0',
    u'Connection': u'keep-alive',
    u'Referer': u'http://www.landchina.com/',
}

common_cookie = {
    u'ASP.NET_SessionId': u'xn3ea0tasijuv1fgi3gsxy5j',
    u'Hm_lvt_83853859c7247c5b03b527894622d3fa': u'1559721714',
    u'Hm_lpvt_83853859c7247c5b03b527894622d3fa': '1554342276',
    u'srcurl': u'687474703a2f2f7777772e6c616e646368696e612e636f6d2f',
    u'yunsuo_session_verify': u'6845bd039f608cff16714b9524ffbe07',
    u'security_session_mid_verify': u'03741145d970672dc0f7a02d42537b96'
}


def update_cookie():
    url = u'http://www.landchina.com'
    ret = requests.request('GET', url, headers=common_headers)
    set_cookie = ret.headers.get('Set-Cookie', None)
    if set_cookie == None:
        return False

    match = re.search(ur'(yunsuo_session_verify)=(.*?);', set_cookie)
    if match:
        common_cookie.update({ match.group(1) : match.group(2) })
        return True

    return False

