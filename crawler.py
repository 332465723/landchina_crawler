# -*- coding: utf-8 -*-

import re
import time
import requests
import urllib2
import random
import StringIO
import gzip
from bs4 import BeautifulSoup
from font_decoder import FontDecoder
from params import CrawlerHeaders

crawler_headers = CrawlerHeaders(cookie_file='input/cookie.txt')
sleep_base_time = 3


def random_sleep():
    return float(sleep_base_time + random.randint(0, 5))


def get_web_html(target_url):
    r = urllib2.Request(target_url, headers=crawler_headers.common_headers)
    response = urllib2.urlopen(r, timeout=10)

    content = response.read()
    content = StringIO.StringIO(content)
    gzipper = gzip.GzipFile(fileobj=content)
    html_text = gzipper.read().decode('gbk')

    match = re.search(ur'styles\/fonts\/(.*.woff)\?', html_text)
    if match:
        try:
            font_url = 'http://landchina.com/styles/fonts/' + match.group(1)
            r = urllib2.Request(font_url, headers=crawler_headers.common_headers)
            response = urllib2.urlopen(r, timeout=10)
            font_content = response.read()
            font_file_path = './download_fonts/%s' % match.group(1)
            with open(font_file_path, 'wb') as fp:
                fp.write(font_content)
            fd = FontDecoder(obj_font_file_path=font_file_path)

            word_map = fd.generate_word_map()
            for code in word_map:
                html_text = html_text.replace(code, word_map[code])
        except Exception as e:
            print('WOFF of target_url[%s] is bad bad!' % target_url)
            print(font_url)
            pass

    crawler_headers.update_cookie_ts(int(time.time()))
    return html_text


def get_jieguo_filter_result_html(jieguo_payload):
    url = u"http://www.landchina.com/default.aspx"
    querystring = {
        u"tabid": u"263",
        u"wmguid": u"75c72564-ffd9-426a-954b-8ac2df0903b7",
        u"p": u""
    }
    response = requests.request("POST", url, data=jieguo_payload, headers=crawler_headers.common_headers, params=querystring)
    return response.text


def extract_jieguo_land_result_from_html(html_obj):
    target_cols = [
        u'行政区',
        u'电子监管号',
        u'项目名称',
        u'项目位置',
        u'面积',
        u'土地来源',
        u'土地用途',
        u'供地方式',
        u'土地使用年限',
        u'行业分类',
        u'土地级别',
        u'成交价格',
        u'土地使用权人',
        u'下限',
        u'上限',
        u'约定交地时间',
        u'约定开工时间',
        u'约定竣工时间',
        u'实际开工时间',
        u'实际竣工时间',
        u'批准单位',
        u'合同签订日期',
        ]

    # html_obj = open('test.html').read().decode('gbk').encode('utf-8')
    soup = BeautifulSoup(html_obj, 'html.parser')

    ret = []
    for tab in soup.find_all('table'):
        tab_class = tab.get('class', None)
        if tab_class is None or u'theme' not in tab_class:
            continue

        kv_arr = []
        for td_obj in tab.find_all('span'):
            val = td_obj.text.strip()
            kv_arr.append(val)

        for col in target_cols:
            found_flag = False
            for idx, item in enumerate(kv_arr):
                if item.find(col) == 0:
                    found_flag = True
                    ret.append((col, kv_arr[idx + 1]))
                    break

            if not found_flag:
                ret.append((col, ''))

    return ret


def jieguo_announcement_digger(jieguo_payload):
    # get filter results
    filter_result_html = get_jieguo_filter_result_html(jieguo_payload)

    # parse all the rows in the filter results
    soup = BeautifulSoup(filter_result_html, 'html.parser')
    rslt = []
    for tr_obj in soup.find_all('tr'):
        tr_class = tr_obj.get('class', None)
        if tr_class is None:
            continue

        rslt_tmp = []
        target_class_arr = (u'gridItem', u'gridAlternatingItem')
        if any([(tmp_class in target_class_arr) for tmp_class in tr_class]):
            td_obj_arr = tr_obj.find_all('td')
            if td_obj_arr[1].find('span') is not None:
                rslt_tmp.append((u'行政区', td_obj_arr[1].find('span')['title']))
            else:
                rslt_tmp.append((u'行政区', td_obj_arr[1].get_text()))
            if td_obj_arr[2].find('span') is not None:
                rslt_tmp.append((u'土地坐落', td_obj_arr[2].find('span')['title']))
            else:
                rslt_tmp.append((u'土地坐落', td_obj_arr[2].get_text()))
            rslt_tmp.append((u'总面积', td_obj_arr[3].get_text()))
            rslt_tmp.append((u'土地用途', td_obj_arr[4].get_text()))
            rslt_tmp.append((u'供应方式', td_obj_arr[5].get_text()))
            rslt_tmp.append((u'签订时间', td_obj_arr[6].get_text()))
            info_tab_url = 'http://www.landchina.com/' + td_obj_arr[2].find('a')['href']
            rslt_tmp.append((u'相关链接', info_tab_url))

            print('accessing %s' % info_tab_url)
            html_text = get_web_html(info_tab_url)
            ret_table = extract_jieguo_land_result_from_html(html_text)

            tmp = []
            for line in rslt_tmp:
                tmp.append(line)
            for line in ret_table:
                tmp.append(line)

            rslt.append(tmp)
            print('inserted an array[%s]' % len(tmp))

            time.sleep(random_sleep())
    return rslt


def extract_churang_land_info_from_html(html_obj):
    target_cols = [
        u'宗地编号',
        u'宗地总面积',
        u'宗地坐落',
        u'出让年限',
        u'容积率',
        u'建筑密度',
        u'绿化率',
        u'建筑限高',
        u'土地用途明细',
        u'投资强度',
        u'保证金',
        u'估价报告备案号',
        u'起始价',
        u'加价幅度',
        u'挂牌开始时间',
        u'挂牌截止时间',
        # u'备注',
        u'现状土地条件',
    ]

    soup = BeautifulSoup(html_obj, 'html.parser')

    all_text = soup.get_text()
    deadline_match = re.search(ur'交纳竞买保证金的截止时间为(\d+年\d+月\d+日\d+时\d+分)', all_text)
    if deadline_match:
        deadline_str = deadline_match.group(1)
    else:
        deadline_str = ''

    ret_table = []
    for tab in soup.find_all('table'):
        tab_border = tab.get('border', None)
        if tab_border != '1':
            continue

        kv_arr = []
        for tr_obj in tab.find_all('tr'):
            for td_obj in tr_obj.find_all('td'):
                val = td_obj.text.strip()
                kv_arr.append(val)

        ret = []
        for col in target_cols:
            found_flag = False
            for idx, val in enumerate(kv_arr):
                if val.find(col) == 0:
                    found_flag = True
                    if col == u'现状土地条件':
                        ret.append((val[:6], val[6:]))
                    else:
                        ret.append((col, kv_arr[idx + 1]))
                    break

            if not found_flag:
                ret.append((col, ''))

        ret.append((u'交纳竞买保证金的截止时间', deadline_str))
        ret_table.append(ret)
    return ret_table


def get_churang_filter_result_html(churang_payload):
    url = u"http://www.landchina.com/default.aspx"
    querystring = {
        u"tabid": u"261",
        u"wmguid": u"20aae8dc-4a0c-4af5-aedf-cc153eb6efdf",
        u"p": u""
    }
    response = requests.request("POST", url, data=churang_payload, headers=crawler_headers.common_headers, params=querystring)
    return response.text


def churange_announcement_digger(churang_payload):
    # get filter results
    filter_result_html = get_churang_filter_result_html(churang_payload)

    # do the parsing job
    soup = BeautifulSoup(filter_result_html, 'html.parser')
    rslt = []
    for tr_obj in soup.find_all('tr'):
        tr_class = tr_obj.get('class', None)
        if tr_class is None:
            continue

        rslt_tmp = []
        target_class_arr = (u'gridItem', u'gridAlternatingItem')
        if any([(tmp_class in target_class_arr) for tmp_class in tr_class]):
            td_obj_arr = tr_obj.find_all('td')
            rslt_tmp.append((u'行政区', td_obj_arr[1].get_text()))
            rslt_tmp.append((u'供应公告标题', td_obj_arr[2].find('span')['title']))
            rslt_tmp.append((u'公告类型', td_obj_arr[3].get_text()))
            rslt_tmp.append((u'发布时间', td_obj_arr[4].get_text()))
            info_tab_url = 'http://www.landchina.com' + td_obj_arr[2].find('a')['href']
            rslt_tmp.append((u'相关链接', info_tab_url))

            print('accessing %s' % info_tab_url)
            html_text = get_web_html(info_tab_url)

            ret_table = extract_churang_land_info_from_html(html_text)
            for tab in ret_table:
                tmp = []
                for line in rslt_tmp:
                    tmp.append(line)
                for line in tab:
                    tmp.append(line)
                rslt.append(tmp)
                print('inserted an array[%s]' % len(tmp))
            time.sleep(random_sleep())

    return rslt

if __name__ == '__main__':
    # UPDATE CONDITION_STR
    # TODO ChuRang
    with open('./input/churang_payload.txt', 'r') as fp:
        churang_payload = fp.read().strip().decode('utf-8')

    # TODO JieGuo
    with open('./input/jieguo_payload.txt', 'r') as fp:
        jieguo_payload = fp.read().strip().decode('utf-8')

    print(u'=' * 30)
    print(u'这是土地出让公告和结果公告查询工具，使用指引：')
    print(u'请更新待查类别的查询文件（churang_payload.txt、jieguo_payload.txt）')
    print(u'=' * 30)

    print(u'输入你需要查询的类别:')
    print(u'1. 出让公告')
    print(u'2. 结果公告')
    print(u'3. 退出')

    input_cmd = raw_input('输入待查类别编码?(1~2)')
    if input_cmd not in ('1', '2'):
        exit(0)
    elif input_cmd == '1':
        output_file_name = raw_input('将输出成TXT格式，请输入输出文件名：churang_output_')
        crawler_headers.common_headers.update(Referer= 'http://www.landchina.com/default.aspx?tabid=261&wmguid=20aae8dc-4a0c-4af5-aedf-cc153eb6efdf&p=')
        rslt = churange_announcement_digger(churang_payload)
        print('%s rows generated!' % len(rslt))
        if len(rslt) > 0:
            with open('./output/churang_output_%s.txt' % output_file_name, 'w') as fp:
                header = u'|'.join([x[0] for x in rslt[0]]) + u'\n'
                fp.write(header.encode('utf-8'))
                for row in rslt:
                    tmp_line = u'|'.join([x[1] for x in row]) + u'\n'
                    fp.write(tmp_line.encode('utf-8'))
    else:
        output_file_name = raw_input('将输出成TXT格式，请输入输出文件名：jieguo_output_')
        crawler_headers.common_headers.update(Referer=u'http://www.landchina.com/default.aspx?tabid=263&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&p=')
        rslt = jieguo_announcement_digger(jieguo_payload)
        print('%s rows generated!' % len(rslt))
        if len(rslt) > 0:
            with open('./output/jieguo_output_%s.txt' % output_file_name, 'w') as fp:
                header = u'|'.join([x[0] for x in rslt[0]]) + u'\n'
                fp.write(header.encode('utf-8'))
                for row in rslt:
                    tmp_line = u'|'.join([x[1] for x in row]) + u'\n'
                    fp.write(tmp_line.encode('utf-8'))
