#! usr/bin/python
#coding=utf-8

import os
import requests
from bs4 import BeautifulSoup
import zipfile
import shutil
def createDir(request_url):
    request_id = request_url.split('/')[-2]
    search_target = request_url.split('/')[-1].split('=')[1].split('&')[0]
    dir = '/'.join([os.getcwd(), '_'.join([search_target, request_id])])
    # dir = os.getcwd()+'/binary'
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)    
    return dir

def getCaseList(request_url):
    case_list=[]
    r = requests.get(request_url)
    # with open(dir + '/' + url.split('/')[-2] + '.html', 'wb') as f:
    #     f.write(r.content)
    #     f.close()

    soup = BeautifulSoup(r.content, 'lxml')
    case_table = soup.find(id='list_div').table.tbody.find_all('tr')
    # print case_table[0].prettify()
    for case in case_table:
        case_dict={}
        case_tds = case.find_all("td") # replace('\n','').replace('\t','')
        case_dict['id'] = case_tds[1].a.string.replace('\n','').replace('\t','').replace('\r','') # encode('utf-8')[:8]
        case_dict['name'] = case_tds[2].get_text().replace('\n','').replace('\t','').replace('\r','')
        case_dict['platform'] = case_tds[3].get_text().replace('\n','').replace('\t','').replace('\r','')
        case_dict['ide'] = case_tds[4].get_text().replace('\n','').replace('\t','').replace('\r','')
        case_dict['target'] = case_tds[5].get_text().replace('\n','').replace('\t','').replace('\r','')
        case_dict['url'] = case_tds[1].a['href'].replace('\n','').replace('\t','').replace('\r','')
        case_list.append(case_dict)
        # print case_dict
        # print len(case_list)
        # print case.find_all("td")[1].a['href']
    # print case_list
    return case_list

def downloadBinary(dir, caseList):
    domain = 'http://10.192.225.198/'
    for i in caseList:
        case_url = domain + i['url']
        # print case_url
        r = requests.get(case_url)
        soup = BeautifulSoup(r.content, 'lxml')
        table_len = len(soup.find(id='form1').div.find_all('table'))
        bin_a = soup.find(id='form1').div.find_all('table')[table_len-1].find_all('tr')[2].td.a #.a['href']

        bin_name = '@'.join([i['ide'], i['target'], bin_a.string])
        # bin_name = bin_name.replace(' ','').replace('\n','')
        print bin_name

        bin_url = '/'.join([domain, bin_a['href']])
        bin_r = requests.get(bin_url)
        # print bin_url, bin_name
        with open(dir + '/' + bin_name, 'wb') as f:
            f.write(bin_r.content)
            f.close()        

def unzipKeil(dir):
    keil_bin = [i for i in os.listdir(dir) if os.path.splitext(i)[1] == '.zip']
    for i in keil_bin:
        f = zipfile.ZipFile(dir+'\\'+i, 'r')
        for k in f.namelist():
            if os.path.splitext(k)[1] == '.hex':
                f.extract(k, dir)
                os.rename('/'.join([dir,k]), '/'.join([dir, os.path.splitext(i)[0] + '.hex']))
                f.close()
                os.remove('/'.join([dir, i]))

def main():
    request_url = 'http://dapeng/dapeng/information/request/15981/?mcuauto_testcase_id=1500212&isreported=blank'
    
    dir = createDir(request_url)
    downloadBinary(dir, getCaseList(request_url))
    unzipKeil(dir)
if __name__ == '__main__':
    main()