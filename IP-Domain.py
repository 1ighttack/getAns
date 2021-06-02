import re
import requests
from fake_useragent import UserAgent
import time
start = time.time()

requests.packages.urllib3.disable_warnings()

ua = UserAgent()

#爱站-域名
headers_aizhan = {
    'Host': 'dns.aizhan.com',
    'User-Agent': ua.random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://dns.aizhan.com/'}

#站长之家-厂商
headers = {
    'Host':'icp.chinaz.com',
    'Connection':'close',
    'Cache-Control':'max-age=0',
    'sec-ch-ua-mobile':'?0',
    'DNT':'1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-User':'?1',
    'Sec-Fetch-Dest':'document',
    'Referer':'https://icp.chinaz.com/baidu.com',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

def aizhan_spider(ip):
    aizhan_url = 'https://dns.aizhan.com/' + str(ip) + '/'
    aizhan_page_r = requests.get(url=aizhan_url, verify=False, headers=headers_aizhan, timeout=None).text
    if '暂无域名解析到该IP' in aizhan_page_r:
    	pass
    else:
    	aizhan_domains = re.findall(r'''rel="nofollow" target="_blank">(.*?)</a>''', aizhan_page_r)
    	for w in aizhan_domains:
            if __name__ == '__main__':
                ips = w
                chinaz_ip = 'https://icp.chinaz.com/' + str(ips)
                p = requests.get(url=chinaz_ip, headers=headers, verify=False, timeout=None)
                sa = p.text
                df = re.findall(r'<a target="_blank" href=".*?">(.*?)</a>', sa)
                cv = str(ip) + '\t' + str(w) + '\t' + str(df)
                with open('result.txt','a') as k:
                    k.write(cv + '\n')
                    


with open('iplist.txt','r+') as f:

    for i in f.readlines():
        r = i.strip('\n')
        we = re.findall(r'\d+.\d+.\d+.\d+',r)
        for ip in we:
                try:
                    aizhan_spider(ip)
                except Exception as error:
                    print(error)
                else:
                    pass

end = time.time()
print("运行时间:",end-start)


'''
Author:light
time：2021/6/1
脚本写的有点简陋，不过实用才最重要。
记录一下人生的第一个脚本，感谢帮助过我的师傅们！！！
'''